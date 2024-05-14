import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_notEqual(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_textType_notEqual(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_equal(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", TextType.BOLD, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT,
                        "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, Text, https://www.boot.dev)", repr(node)
        )

    def test_textNode(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leafNode = LeafNode("b", "This is a text node")
        self.assertEqual(
            node.text_node_to_html_node().to_html(), leafNode.to_html())


if __name__ == "__main__":
    unittest.main()
