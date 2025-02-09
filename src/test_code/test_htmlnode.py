import unittest
from src.htmlnode import HTMLNode
from src.textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "hello, world",
            None,
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
        )
    
    def test_values(self):
        node = HTMLNode("div", "I wish I could Read",)
        self.assertEqual(
            node.tag, "div"
        )

        self.assertEqual(
            node.value, "I wish I could Read"
        )
        self.assertEqual(
            node.props, None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
    











