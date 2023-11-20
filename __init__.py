from .create_n_token_node import CreateNTokenStringNode
from .join_string_node import JoinStringsNode
from .split_string_node import SplitStringNode
from .join_string_list_node import JoinStringListNode
from .join_string_list_n_element_node import JoinStringListNElementNode

NODE_CLASS_MAPPINGS = {
    "Text Utils - String Subparts": CreateNTokenStringNode,
    "Text Utils - Join Strings": JoinStringsNode,
    "Text Utils - Split String to List": SplitStringNode,
    "Text Utils - Join String List": JoinStringListNode,
    "Text Utils - Join String List N-Elements": JoinStringListNElementNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text Utils - String Subparts": "String Subparts",
    "Text Utils - Join Strings": "Join Strings",
    "Text Utils - Split String to list": "Split String to List",
    "Text Utils - Join String List": "Join String List to one string",
    "Text Utils - Join String List N-Elements": "Join N-Element of String List to one string",
}
