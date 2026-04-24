import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("tag", "value")
        self.assertEqual(str(node), str({ "tag": "tag", "value": "value", "props": None}))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()
    

    
if __name__ == "__main__":
    unittest.main()