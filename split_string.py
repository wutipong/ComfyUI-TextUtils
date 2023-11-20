class SplitStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": "/"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    OUTPUT_IS_LIST = (True, )
    FUNCTION = "perform_split_string"
    CATEGORY = "text utility"

    def perform_split_string(self, text, separator):
        return (text.split(separator), )
