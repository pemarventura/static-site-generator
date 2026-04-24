

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):

        dictionary = {
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "props": self.props_to_html()
        }

        return str(dictionary)
    
    def to_html(self):
        raise NotImplementedError("This should be override by the child class")

    def props_to_html(self):
        if self.props:
            result = ""
            
            for key, value in self.props.items():
                result += f' {key}="{value}"'

            return result
        return None
    
