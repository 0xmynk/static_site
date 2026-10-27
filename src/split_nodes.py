import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =[]

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_parts = old_node.text.split(delimiter)

        if len(split_parts) % 2 ==0:
            raise ValueError(f"Invalid Markdown syntax: missing closing delimiter '{delimiter}'")

        split_nodes = []
        for i, part in enumerate(split_parts):
            if part == "":
              continue

            if i % 2 == 0:
                split_nodes.append(TextNode(part, TextType.TEXT))
            else:
                split_nodes.append(TextNode(part, text_type))

        new_nodes.extend(split_nodes)
    return new_nodes 

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    # Matches [anchor](url) only when NOT preceded by !
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

