import unittest
from src.textnode import TextNode, TextType

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

# return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
if __name__ == '__main__':
    unittest.main()




