import re
from html import unescape

def clean_html_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def shorten_text(text: str, max_length: int = 300) -> str:
    if len(text) <= max_length:
        return text

    return text[:max_length].rsplit(" ", 1)[0] + "..."