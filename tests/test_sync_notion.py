import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import sync_notion


class MarkdownValidationTests(unittest.TestCase):
    def test_accepts_complete_markdown(self):
        payload = {
            "object": "page_markdown",
            "markdown": "# Clase\n\nUna tabla <table><tr><td>1</td></tr></table>\n",
            "truncated": False,
            "unknown_block_ids": [],
        }
        self.assertEqual(
            sync_notion.validate_markdown(payload, "Clase"),
            "# Clase\n\nUna tabla <table><tr><td>1</td></tr></table>\n",
        )

    def test_rejects_incomplete_and_temporary_media(self):
        for payload in [
            {"object": "page_markdown", "markdown": "# Clase", "truncated": True},
            {"object": "page_markdown", "markdown": '<unknown url="x"/>', "truncated": False},
            {"object": "page_markdown", "markdown": "![figura](https://example.com/a.png)", "truncated": False},
        ]:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                sync_notion.validate_markdown(payload, "Clase")

    def test_failed_fetch_does_not_change_any_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "notion" / "01 Matemáticas"
            folder.mkdir(parents=True)
            (folder / "a.md").write_text("original\n", encoding="utf-8")
            (folder / "b.md").write_text("original\n", encoding="utf-8")
            manifest = [
                {"notion_id": "a", "source": "notion/01 Matemáticas/a.md", "title": "A"},
                {"notion_id": "b", "source": "notion/01 Matemáticas/b.md", "title": "B"},
            ]
            (root / "course_pages.json").write_text(json.dumps(manifest), encoding="utf-8")

            def fake_fetch(page_id, token):
                if page_id == "b":
                    raise RuntimeError("API failure")
                return {"object": "page_markdown", "markdown": "# Changed", "truncated": False}

            with patch.object(sync_notion, "ROOT", root), patch.object(
                sync_notion, "fetch_markdown", side_effect=fake_fetch
            ), patch.dict("os.environ", {"NOTION_TOKEN": "test-token"}):
                with self.assertRaises(RuntimeError):
                    sync_notion.sync()

            self.assertEqual((folder / "a.md").read_text(), "original\n")
            self.assertEqual((folder / "b.md").read_text(), "original\n")


if __name__ == "__main__":
    unittest.main()
