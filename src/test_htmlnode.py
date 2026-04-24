import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("tag", "value")
        self.assertEqual(str(node), str({ "tag": "tag", "value": "value","children": None, "props": None}))

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props = {"prop1": "something", "prop2": "otherthing"})
        self.assertEqual(node.props_to_html(), ' prop1="something" prop2="otherthing"')
    
if __name__ == "__main__":
    unittest.main()