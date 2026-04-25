import re
from textnode import TextType, TextNode
from leafnode import LeafNode


def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.PLAIN_TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD_TEXT:
                return LeafNode("<b>", text_node.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("<i>", text_node.text)
            case TextType.CODE_TEXT:
                return LeafNode("<code>", text_node.text)
            case TextType.LINK_TEXT:
                return LeafNode("<a>", text_node.text, {"href": text_node.url} )
            case TextType.IMAGE_TEXT:
                return LeafNode("<img>", "", {"src": text_node.url, "alt": text_node.text} )
            case _:
                raise Exception("Text node must have a type of text")
            
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if old_nodes and delimiter and text_type:
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                new_nodes.append(node)
            else:
                parts = node.text.split(delimiter)
                if len(parts) % 2 == 0:
                    raise Exception("Invalid markdown syntax")
                for i, part in enumerate(parts):
                    if part == "":
                        continue
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.PLAIN_TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        return new_nodes
    return old_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    if old_nodes:
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                new_nodes.append(node)
            else:
                markdowns = extract_markdown_images(node.text)

                if not markdowns:
                    new_nodes.append(node)
                    continue

                text = node.text
                for markdown in markdowns:
                    pattern = f"![{markdown[0]}]({markdown[1]})"
                    parts = text.split(pattern, 1)

                    if parts[0] != "":
                        new_nodes.append(TextNode(text=parts[0], text_type=TextType.PLAIN_TEXT))

                    new_nodes.append(TextNode(text=markdown[0], text_type=TextType.IMAGE_TEXT, url=markdown[1]))

                    text = parts[1] if len(parts) > 1 else ""

                if text != "":
                    new_nodes.append(TextNode(text=text, text_type=TextType.PLAIN_TEXT))

        return new_nodes
    return old_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK_TEXT, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
