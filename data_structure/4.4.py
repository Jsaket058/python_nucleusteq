# 4. Create a function that counts the frequency of each word in a list.

def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = count_word_frequency(word_list)
print(result)
