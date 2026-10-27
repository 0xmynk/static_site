class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props= None):       
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, val in self.props.items():
            props_str += f' {key}="{val}"'
        return props_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

