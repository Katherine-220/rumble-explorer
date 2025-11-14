thonpython
def detect_input_type(value: str) -> str:
    if "video" in value or "/v" in value:
        return "video"
    if "/c/" in value:
        return "channel"
    return "unknown"