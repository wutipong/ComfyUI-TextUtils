from .create_n_token_node import CreateNTokenStringNode
from .join_string_node import JoinStringsNode
NODE_CLASS_MAPPINGS = {
    "Text Utils - String Subparts": CreateNTokenStringNode,
    "Text Utils - Join Strings": JoinStringsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text Utils - String Subparts": "String Subparts",
    "Text Utils - Join Strings": "Join Strings",
}
