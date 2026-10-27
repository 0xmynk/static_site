from textnode import TextNode, TextType
from split_nodes import extract_markdown_images, extract_markdown_links, split_nodes_delimiter


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text
        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"
            sections = current_text.split(image_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text
        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            sections = current_text.split(link_markdown, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
