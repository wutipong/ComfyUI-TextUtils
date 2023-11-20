class JoinStringListNElementNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "texts": ("STRING", {"forceInput": True}),
                "separator": ("STRING", {"default": "/"}),
                "n": ("INT", {"default": 1, "min": 0, "max": 10000, "step": 1}),
                "start_from": (["front", "back"],)
            },
        }
    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "perform_join_string_list"
    CATEGORY = "text utility"

    def perform_join_string_list(self, texts, separator, n, start_from):
        separator = separator[0]
        n = n[0]
        start_from = start_from[0]

        start = 0
        end = n

        if start_from == "back":
            end = len(texts)
            start = end - n
            if start < 0:
                start = 0

        return (separator.join(texts[start: end]), )
