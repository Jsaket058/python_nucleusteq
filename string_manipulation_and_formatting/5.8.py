# 8. Create a function to remove HTML tags from a string.

import re

def remove_html_tags(text):
    """
    Remove HTML tags from the given string.

    Args:
        text (str): A string that may contain HTML tags.

    Returns:
        str: String with all HTML tags removed.
    """
    clean_text = re.sub(r'<[^>]+>', '', text)
    return clean_text

html_string = "<h1>Welcome</h1><p>This is <b>bold</b> text.</p>"
plain_text = remove_html_tags(html_string)
print(plain_text)  # Output: WelcomeThis is bold text.
