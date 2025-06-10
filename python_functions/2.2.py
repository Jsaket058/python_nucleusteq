def is_palindrome(s: str) -> bool:
    cleaned = s.lower()
    return cleaned == cleaned[::-1]
