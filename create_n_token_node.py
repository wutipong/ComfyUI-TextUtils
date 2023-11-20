import textutils


class CreateNTokenStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { 
                "text" : ("TEXT", ""),
                "delim": ("TEXT", ""),
                "n": ("INT", 0) 
            },
        }

    RETURN_TYPES = ("Text",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "create_n_token_string"
    CATEGORY = "wutipong"

    def create_n_token_string(self, text, delim, n):
        return (textutils.create_n_token_string(text, delim, n),)