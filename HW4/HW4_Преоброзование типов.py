# 1
# Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

my_str = "Robin Singh".split()
another_str = "I love arrays they are my favorite".split()

print(my_str,another_str)

# 2
# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

my_list = ['Ivan', 'Ivanou']
first_str = 'Minsk'
thecond_str = 'Belarus'
dasda = "Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus"

print(f"Привет, {my_list[0]} {my_list[1]}! Добро пожаловать в {first_str} {thecond_str}")

# 3
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

list_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]

list_to_str = ' '.join(list_1)

print(list_to_str)

# 4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

list_HW_4 = [1, "hello", 3.14, True, 5, "world", 7.5, False, "Python", 10]

list_HW_4.insert(2, 'danik')
list_HW_4.pop(6)

print(list_HW_4)

#5
#Есть 2 словаря
#a = { 'a': 1, 'b': 2, 'c': 3}
#b = { 'c': 3, 'd': 4,'e': 5}
#Необходимо их объединить по ключам, а значения ключей поместить в список, если у
#одного словаря есть ключ "а", а у другого нету, то поставить значение None на
#соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
#ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

dict_a = {
    'a': 1,
    'b': 2,
    'c': 3
}
dict_b = {
    'c': 3,
    'd': 4,
    'e': 5
}

dict_ab = {}

all_keys = set(dict_a.keys()).union(dict_b.keys())

for key in all_keys:
    dict_ab[key] = [dict_a.get(key), dict_b.get(key)]

print(dict_ab)

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

massive_int = [1, 5, 2, 9, 2, 9, 1]

uniq = 0
for i in massive_int:
    uniq ^= i
print(uniq)

# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам
# необходимо найти самую частую букву в тексте. Результатом должна быть буква в
# нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете
# считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
# пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет
# буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по
# одному разу, так что мы выбираем "e".
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o"
# "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"



