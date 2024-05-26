# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

def get_longest_word(string):
    words = string.split()
    longest_word = max(words, key = len)
    return longest_word
print(get_longest_word('dsadasdsaasdasdasdasdas sdasdfdsfafasfas 321113333333333333333333333333333'))