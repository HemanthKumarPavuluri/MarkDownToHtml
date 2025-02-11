import unittest
from src.textnode import TextNode, TextType, text_node_to_html_node
from src.htmlnode import LeafNode

class TextTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node1 = TextNode("Bold", TextType.LINK, "https://superuser.com")
        node2 = TextNode("Bold", TextType.LINK, "https://superuser.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Hello", TextType.BOLD, "https://example.com")
        expected_repr = "TextNode(Hello, bold, https://example.com)"
        self.assertEqual(repr(node), expected_repr)


class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a text node")

    def test_image(self):
        node = TextNode("this is an image", TextType.IMAGE, "https://myimage.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://myimage.jpg","alt": "this is an image"})



if __name__ == '__main__':
    unittest.main()




