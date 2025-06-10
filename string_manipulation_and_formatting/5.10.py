# 10. Implement a string compression algorithm (e.g., aabcccccaaa -> a2b1c5a3).

def compress_string(s):
    """
    Compress a string using counts of repeated characters.

    Args:
        s (str): Input string to compress.

    Returns:
        str: Compressed version of the string.
    """
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1 
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))

    result = ''.join(compressed)

    # Optional: Return original if compressed is not shorter
    return result if len(result) < len(s) else s

print(compress_string("aabcccccaaa"))  
print(compress_string("abc"))          
print(compress_string(""))             
