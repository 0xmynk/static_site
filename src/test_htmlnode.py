import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_standard(self):
        node = HTMLNode(
            tag="a",
            value="Boot.dev",
            props={
                "href": "https://www.boot.dev",
                "target": "_blank",
            },
        )
        self.assertEqual(
                node.props_to_html(),
                ' href="https://www.boot.dev" target="_blank"',
                )
    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="h1", value="Title", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="p", value = "Test paragraph")
        self.assertIn("Test paragraph", repr(node))

if __name__ == "__main__":
     unittest.main()
