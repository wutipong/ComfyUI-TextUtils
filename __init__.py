from .join_string_node import JoinStringsNode
from .split_string_node import SplitStringNode
from .join_string_list_node import JoinStringListNode
from .join_string_list_n_element_node import JoinStringListNElementNode

NODE_CLASS_MAPPINGS = {
    "Text Utils - Join Strings": JoinStringsNode,
    "Text Utils - Split String to List": SplitStringNode,
    "Text Utils - Join String List": JoinStringListNode,
    "Text Utils - Join N-Elements of String List": JoinStringListNElementNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text Utils - Join Strings": "Join Strings",
    "Text Utils - Split String to List": "Split String to List",
    "Text Utils - Join String List": "Join String List",
    "Text Utils - Join N-Elements of String List": "Join N-Element of String List",
}
