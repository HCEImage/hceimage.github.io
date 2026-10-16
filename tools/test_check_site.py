"""Small parser regressions; run with python3 -m unittest discover -s tools."""

import unittest

from check_site import Page, markdown_policy, normalized_text


class SiteParserTest(unittest.TestCase):
    def test_duplicate_anchors_are_not_silently_overwritten(self):
        page = Page('<h1 id="one">Title</h1><h2 id="one">Duplicate</h2>')
        self.assertEqual({"one"}, page.duplicates)
        self.assertEqual(1, page.h1_count)

    def test_references_and_escaped_json_are_preserved(self):
        page = Page(
            '<a href="/guide/#field">Guide</a>'
            '<pre><code>{"name":"&lt;example&gt;"}</code></pre>'
        )
        self.assertEqual(["/guide/#field"], page.references)
        self.assertEqual([{"name": "<example>"}], page.json_examples)

    def test_policy_comparison_ignores_presentation_not_words(self):
        page = Page(
            '<nav>Other text</nav><div class="policy-content"><h2>Scope</h2>'
            '<p>Local <strong>only</strong>.</p></div><footer>Footer</footer>'
        )
        markdown = "# Policy\n\n**Effective date: today**\n\n## Scope\n\nLocal **only**.\n"
        self.assertEqual(markdown_policy(markdown), normalized_text("".join(page.policy)))
        self.assertNotEqual(
            markdown_policy(markdown.replace("only", "upload")),
            normalized_text("".join(page.policy)),
        )

    def test_policy_lead_is_included_without_title_or_effective_date(self):
        page = Page(
            '<header class="policy-header"><h1>Policy</h1>'
            '<p class="effective-date">Today</p><p class="lead">Local tool.</p></header>'
            '<div class="policy-content"><h2>Scope</h2><p>No upload.</p></div>'
        )
        self.assertEqual("Local tool. Scope No upload.", normalized_text("".join(page.policy)))


if __name__ == "__main__":
    unittest.main()
