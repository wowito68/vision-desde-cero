"""Generate Just the Docs pages from the Markdown snapshots in notion/."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = json.loads((ROOT / "course_pages.json").read_text(encoding="utf-8"))

for page in PAGES:
    source = ROOT / page["source"]
    target = ROOT / page["target"]
    content = source.read_text(encoding="utf-8").strip()

    if page["permalink"] == "/":
        content += '\n\n[Comenzar por matemáticas]({{ "/matematicas/" | relative_url }})\n'
    elif page["permalink"] == "/matematicas/":
        content += '\n\n[Ir a la primera clase]({{ "/matematicas/numeros-variables-y-funciones/" | relative_url }})\n'

    front = [
        "---",
        f"title: {json.dumps(page['title'], ensure_ascii=False)}",
        f"layout: {'home' if page['permalink'] == '/' else 'default'}",
        f"nav_order: {page['order']}",
        f"permalink: {page['permalink']}",
    ]
    if page["parent"]:
        front.append(f"parent: {json.dumps(page['parent'], ensure_ascii=False)}")
    front.extend(["---", ""])

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(front) + content + "\n", encoding="utf-8")
    print(target.relative_to(ROOT))
