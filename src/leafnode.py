from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):

        dictionary = {
            "tag": self.tag,
            "value": self.value,
            "props": self.props_to_html()
        }

        return str(dictionary)
    
    