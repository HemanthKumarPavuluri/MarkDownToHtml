from src.textnode import TextNode, TextType
import re
"""
splitting nodes based on delimiter and returning a list of TextNodes
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 ==0:
            raise ValueError("invalid markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

"""
Extracting markdown images from text
"""

def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    match = re.findall(regex, text)
    return match
"""
Extracting markdown links from text
"""

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    match = re.findall(regex, text)
    return match

"""
this method splits the TextNodes list into 
individual TextTypes seperating images
"""
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        original_text = node.text
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            alt, url = image
            start = original_text.index(f"![{alt}]({url})")
            end = start + len(f"![{alt}]({url})")
            if start > 0:
                new_nodes.append(TextNode(original_text[:start], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            original_text = original_text[end:]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


"""
this method splits the TextNodes list into 
individual TextTypes seperating Links
"""
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        original_text = node.text
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            alt, url = link
            start = original_text.index(f"[{alt}]({url})")
            end = start + len(f"[{alt}]({url})")
            if start > 0:
                new_nodes.append(TextNode(original_text[:start], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            original_text = original_text[end:]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


"""
convert a raw string of markdown-flavored text into a list of TextNode objects.
"""
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes








