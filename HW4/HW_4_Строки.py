# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.

my_str = 'Testirovanie'

print(my_str[0],my_str[-1],my_str[2],my_str[-3])
print(len(my_str))

# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ●
# первые восемь символов
# ●
# четыре символа из центра строки
# ●
# символы с индексами кратными трем
# ●
# переверните строку

another_str = 'Automation test'

print(another_str[0:8])
print(another_str[6:10])
print(another_str[::3])
print(another_str[::-1])

# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.

my_name = "my name is name"
real_name = 'Danik'
original_str = "my name is name"

list_name = my_name.split()

list_name[3] = real_name

print(' '.join(list_name))

# 4 Есть строка: test_tring = "Hello world!", необходимо
# ●
# напечатать на каком месте находится буква w
# ●
# кол-во букв l
# ●
# Проверить начинается ли строка с подстроки: “Hello”
# ●
# Проверить заканчивается ли строка подстрокой: “qwe”

test_tring = "Hello world!"

print(test_tring.index('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))
