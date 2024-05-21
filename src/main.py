from inline_markdown import split_nodes_images
from markdown_blocks import markdown_to_blocks


def main():
    text = """ 
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    new_nodes = markdown_to_blocks(text)


main()
