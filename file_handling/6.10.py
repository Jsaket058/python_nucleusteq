# 10. Create a function to replace specific words in a file with user-provided values.

def replace_words_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()

    for old_word, new_word in replacements.items():
        content = content.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(content)

replacements = {
    "Saket": "sahil",
    "Hello": "Hi",
    "how": "When"
}

replace_words_in_file('file_handling/yo.txt', replacements)
