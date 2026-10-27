from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BlockType.HEADING

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        is_quote = True
        for line in lines:
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE

    if block.startswith("- "):
        is_unordered = True
        for line in lines:
            if not line.startswith("- "):
                is_unordered = False
                break
        if is_unordered:
            return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        is_ordered = True
        i = 1
        for line in lines:
            expected_prefix = f"{i}. "
            if not line.startswith(expected_prefix):
                is_ordered = False
                break
            i += 1
        if is_ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks
