from .textutils import create_n_token_string


class CreateNTokenStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": "/"}),
                "n": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "perform_create_n_token_string"
    CATEGORY = "text utility"

    def perform_create_n_token_string(self, text, delim, n):
        return (create_n_token_string(text, delim, n),)
