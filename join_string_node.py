class JoinStringsNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"default": ""}),
                "text2": ("STRING", {"default": ""})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "perform_join_strings"
    CATEGORY = "text utility"

    def perform_join_strings(self, text1, text2):
        return (text1 + text2, )
