from .textutils import create_n_token_string


class CreateNTokenStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": "/"}),
                "n": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "start_from": (["front", "back"],)
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "perform_create_n_token_string"
    CATEGORY = "text utility"

    def perform_create_n_token_string(self, text, separator, n, start_from):
        if start_from == "back":
            n = -n

        return (create_n_token_string(text, separator, n),)
