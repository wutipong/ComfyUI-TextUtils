from .create_n_token_node import CreateNTokenStringNode
from .join_string_node import JoinStringsNode
from .split_string import SplitStringNode

NODE_CLASS_MAPPINGS = {
    "Text Utils - String Subparts": CreateNTokenStringNode,
    "Text Utils - Join Strings": JoinStringsNode,
    "Text Utils - Split String to List": SplitStringNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text Utils - String Subparts": "String Subparts",
    "Text Utils - Join Strings": "Join Strings",
    "Text Utils - Split String to list": "Split String to List",
}
