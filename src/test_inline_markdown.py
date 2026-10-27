import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link, text_to_textnodes


class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_image_at_start(self):
        node = TextNode(
            "![first](https://boot.dev/first.png) then some text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("first", TextType.IMAGE, "https://boot.dev/first.png"),
            TextNode(" then some text", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_nodes_no_links_or_images(self):
        node = TextNode("Just plain text with nothing special", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node]), [node])
        self.assertListEqual(split_nodes_image([node]), [node])

    def test_non_text_nodes_preserved(self):
        code_node = TextNode("print('hello')", TextType.CODE)
        self.assertListEqual(split_nodes_link([code_node]), [code_node])
        self.assertListEqual(split_nodes_image([code_node]), [code_node])
class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image",
                TextType.IMAGE,
                "https://i.imgur.com/fJRm4Vk.jpeg",
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(nodes, expected)

    def test_plain_text(self):
        text = "Just plain text without markdown"
        nodes = text_to_textnodes(text)
        expected = [TextNode("Just plain text without markdown", TextType.TEXT)]
        self.assertListEqual(nodes, expected)

    def test_multiple_formatting_instances(self):
        text = "**bold 1** and **bold 2** with *italic 1* and *italic 2*"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("bold 1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold 2", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("italic 1", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic 2", TextType.ITALIC),
        ]
        self.assertListEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()


