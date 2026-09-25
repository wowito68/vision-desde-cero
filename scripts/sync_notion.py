"""Read selected Notion course pages as Markdown and update notion/ snapshots.

Requires NOTION_TOKEN from a read-only internal Notion connection shared with
the course page. The token is never written to disk or printed.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API_VERSION = "2026-03-11"
API_ROOT = "https://api.notion.com/v1/pages"
MAX_RESPONSE_BYTES = 8 * 1024 * 1024


def validate_markdown(payload: dict, label: str) -> str:
    if payload.get("object") != "page_markdown":
        raise ValueError(f"{label}: Notion did not return a page_markdown object")
    if payload.get("truncated") or payload.get("unknown_block_ids"):
        raise ValueError(f"{label}: Notion returned incomplete content")
    markdown = payload.get("markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise ValueError(f"{label}: Notion returned empty Markdown")

    # Enhanced Markdown tags for these block types do not render reliably in
    # Jekyll. Stop the sync rather than publishing broken links or private
    # pre-signed media URLs. Add an explicit converter before using them.
    unsupported = re.search(
        r"<(?:unknown|page|database|file|video|audio|pdf|columns|column|synced_block)\b",
        markdown,
        flags=re.IGNORECASE,
    )
    if unsupported:
        raise ValueError(f"{label}: unsupported Notion block {unsupported.group(0)}")
    if re.search(r"!\[[^\]]*\]\(", markdown):
        raise ValueError(f"{label}: image needs a persistent asset converter")
    if re.search(r"https?://[^\s)]+(?:amazonaws\.com|notionusercontent\.com)", markdown):
        raise ValueError(f"{label}: expiring Notion media URL")
    return markdown.strip() + "\n"


def fetch_markdown(page_id: str, token: str) -> dict:
    request = Request(
        f"{API_ROOT}/{page_id}/markdown",
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": API_VERSION,
            "Accept": "application/json",
        },
    )
    for attempt in range(4):
        try:
            with urlopen(request, timeout=30) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
                if len(raw) > MAX_RESPONSE_BYTES:
                    raise ValueError("Notion response is too large")
                return json.loads(raw)
        except HTTPError as exc:
            if exc.code not in (429, 500, 503, 504, 529) or attempt == 3:
                raise RuntimeError(f"Notion API returned HTTP {exc.code}") from None
            retry_after = exc.headers.get("Retry-After")
            delay = min(float(retry_after), 30) if retry_after else 2 ** attempt
            time.sleep(delay)
        except URLError:
            if attempt == 3:
                raise RuntimeError("Notion API is unreachable") from None
            time.sleep(2 ** attempt)
    raise RuntimeError("Notion API retry limit exceeded")


def sync() -> int:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        raise ValueError("NOTION_TOKEN is missing")
    pages = json.loads((ROOT / "course_pages.json").read_text(encoding="utf-8"))
    updates: list[tuple[Path, str]] = []
    for page in pages:
        if not page["notion_id"]:
            continue
        source = ROOT / page["source"]
        if source.resolve().parent != (ROOT / "notion" / "01 Matemáticas").resolve():
            raise ValueError(f"Unexpected source path: {page['source']}")
        content = validate_markdown(
            fetch_markdown(page["notion_id"], token), page["title"]
        )
        updates.append((source, content))

    # Fetch and validate every page before changing any file.
    changed = 0
    for source, content in updates:
        if not source.exists() or source.read_text(encoding="utf-8") != content:
            source.write_text(content, encoding="utf-8")
            changed += 1
            print(f"Updated {source.relative_to(ROOT)}")
    print(f"Notion sync complete: {changed} page(s) changed")
    return changed


if __name__ == "__main__":
    try:
        sync()
    except (RuntimeError, ValueError) as error:
        print(f"Notion sync stopped: {error}", file=sys.stderr)
        raise SystemExit(1)
