import re

def clean_subtitle_text(subtitle_text):
    # Remove timestamps using regex (example format: [00:01:01 --> 00:01:05])
    subtitle_text = re.sub(r'\[\d{2}:\d{2}:\d{2}\s*-->.*?\]', '', subtitle_text)
    # Remove non-alphanumeric characters and excess spaces
    subtitle_text = re.sub(r'[^a-zA-Z0-9\s]', '', subtitle_text)
    subtitle_text = subtitle_text.strip().lower()
    return subtitle_text
