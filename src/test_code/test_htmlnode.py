import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_html_no_children(self):
        node = LeafNode("p", "hello world")
        self.assertEqual(node.to_html(), "<p>hello world</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")

    def test_to_html_with_children(self):
        child_node = LeafNode("p", "Hello mike testing")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>Hello mike testing</p></div>")
    
    def test_to_html_with_multiple_children(self):
        grand_child = LeafNode("span", "Hello jack")
        child_node = ParentNode("p", [grand_child])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><span>Hello jack</span></p></div>")
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


if __name__ == '__main__':
    unittest.main()










