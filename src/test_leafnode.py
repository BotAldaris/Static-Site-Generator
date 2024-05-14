import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_error(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)
