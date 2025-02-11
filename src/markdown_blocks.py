from src.htmlnode import (
    ParentNode,
    )
from src.inline_markdown import text_to_textnodes
from src.textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks  

"""
block to blocktype
supporting 6 types
paragraph
heading
code
quote
unordered_list
ordered_list
""" 

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    if block.lstrip().startswith("#"):
        return block_type_heading
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist

    return block_type_paragraph
    

"""
converts a full markdown document into a single parent HTMLNode. 
That one parent HTMLNode should of course contain many child HTMLNode objects representing the nested elements.
"""
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []

    for block in markdown_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return praragraph_to_htmlnode(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def praragraph_to_htmlnode(block):
    lines = block.split("\n")
    para = " ".join(lines)
    children = text_to_children(para)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = block.count("#")
    if len(block) <= level + 1:
        raise ValueError("incorrect heading level")
    text = block[level+1:]
    children  = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        olist = ParentNode("li", children)
        html_items.append(olist)
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    text_content = " ".join(new_lines)
    children = text_to_children(text_content)
    return ParentNode("blockquote", children)










