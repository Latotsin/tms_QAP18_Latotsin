def get_most_frequent_word(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_frequent = max(word_count, key=word_count.get)
    return most_frequent

print(get_most_frequent_word("apple orange apple banana apple orange"))

