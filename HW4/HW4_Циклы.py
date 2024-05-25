# 1
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.

a = 15
b = 20
summa = 0

for i in range(a, b +1):
    summa += i
print(summa)

# 2
# Найти сумму всех натуральных чисел в от A до B

first_num = -6
thecond_num = 10

sum_num = 0

for x in range(first_num,thecond_num):
    sum_num += x
print(sum_num)

# 3
# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.

numbers = [10, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positives = 1
negatives = 0
count_of_negatives = 0

for number in numbers:
    if number > 0:
        positives *= number
    elif number < 0:
        negatives += number
        count_of_negatives += 1
print(positives)
print(negatives)
print(count_of_negatives)

# 4
# Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

new_dict = {
    'Бекиш Александр': 21.07,
    'Будник Алексей': 20.34,
    'Гребень Анастасия': 22.12,
    'Давидович Татьяна': 30,
    'Дешук Дмитрий': 24.01,
    'Казак Анна': 28.17
}

best_result = float('inf')

for time in new_dict.values():
    if time < best_result:
        best_result = time
print(best_result)

# 5
# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число

my_list = [1, 5, 2, 9, 2, 9, 1]

for r in my_list:
    if my_list.count(r) == 1:
        print(r)