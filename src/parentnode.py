from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):

        if not self.tag:
            raise ValueError("Parent node must have a tag")

        if not self.children:
            raise ValueError("Parent node must have children")

        children_str = " ".join([child.to_html() for child in self.children])
        
        return f"<{self.tag}>{children_str}</{self.tag}>"