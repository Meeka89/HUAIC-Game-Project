"""Checks for the current documentation repository; no engine dependencies."""

from pathlib import Path
import re
import subprocess
import unicodedata
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def without_fences(text):
    """Ignore examples inside Markdown fenced code blocks."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def heading_ids(text):
    counts = {}
    ids = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", without_fences(text), re.M):
        slug = "".join(
            char for char in heading.lower()
            if char in "-_ " or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        ids.add(f"{slug}-{number}" if number else slug)
    return ids


class RepositoryChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use the Git index so ignored files and unrelated local drafts cannot
        # accidentally make a missing link pass locally but fail on GitHub.
        result = subprocess.run(
            ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
        )
        cls.tracked = set(result.stdout.decode("utf-8").rstrip("\0").split("\0"))

    def test_internal_markdown_links(self):
        for name in sorted(self.tracked):
            if not name.endswith(".md"):
                continue
            source = ROOT / name
            text = without_fences(source.read_text(encoding="utf-8"))
            for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\s]+)\)", text):
                target = match[1].strip("<>")
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue  # External services are not part of this check.
                with self.subTest(source=name, target=target):
                    base = ROOT if url.path.startswith("/") else source.parent
                    resolved = (base / unquote(url.path).lstrip("/")).resolve() if url.path else source
                    self.assertTrue(resolved.is_relative_to(ROOT), "Link leaves repository")
                    relative = resolved.relative_to(ROOT).as_posix()
                    if resolved.is_dir():
                        self.assertTrue(any(p.startswith(relative + "/") for p in self.tracked),
                                        "Linked directory has no tracked files")
                    else:
                        self.assertIn(relative, self.tracked, "Missing or incorrectly cased tracked target")
                        self.assertTrue(resolved.is_file(), "Linked file is missing")
                    if url.fragment and relative.endswith(".md"):
                        self.assertIn(unquote(url.fragment), heading_ids(resolved.read_text(encoding="utf-8")),
                                      "Missing heading anchor")

    def test_issue_template_metadata(self):
        names = set()
        templates = sorted(p for p in self.tracked
                           if p.startswith(".github/ISSUE_TEMPLATE/") and p.endswith(".md"))
        self.assertTrue(templates, "No Markdown issue templates found")
        for path in templates:
            with self.subTest(template=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(front, "Missing YAML front matter")
                # The existing Markdown templates use simple scalar metadata.
                for key in ("name", "about"):
                    value = re.search(rf"^{key}:[ \t]*(\S[^\n]*)$", front[1], re.M)
                    self.assertIsNotNone(value, f"Missing {key} metadata")
                    self.assertTrue(value[1].strip("\"' "), f"Empty {key}")
                    if key == "name":
                        self.assertNotIn(value[1], names, "Duplicate template name")
                        names.add(value[1])


if __name__ == "__main__":
    unittest.main()
