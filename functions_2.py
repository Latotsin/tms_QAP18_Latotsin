# "1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

def find_numbers(filename):
    file = open(filename, 'r')
    numbers = file.read().strip().split()
    file.close()

    if len(numbers) < 3:
        print("Ошибка: в файле меньше трех элементов")
    else:
        print(f"Первый элемент: {numbers[0]}")
        print(f"Второй элемент: {numbers[1]}")
        print(f"Предпоследний элемент: {numbers[-2]}")
        print(f"Последний элемент: {numbers[-1]}")

find_numbers('numbers.txt')

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

def split_even_odd(filename):
    odd_numbers_file = open("odd numbers.txt", "w")
    even_numbers_file = open("even numbers.txt", "w")

    with open(filename, 'r') as file:
        numbers = file.read().strip().split()

    for num in numbers:
        if int(num) % 2 == 0:
            even_numbers_file.write(num + ' ')
        else:
            odd_numbers_file.write(num + ' ')

    odd_numbers_file.close()
    even_numbers_file.close()

split_even_odd('numbers.txt')

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

def square_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            squared_line = ' '.join(str(float(num) ** 2) for num in line.strip().split())
            file.write(squared_line)

square_numbers('square numbers.txt')

# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
# - Все делать с помощью функции

def bin_files (file1, file2):
    with open(file1, 'rb') as file1:
        data1 = file1.read()
    with open(file2, 'rb') as file2:
        data2 = file2.read()
    with open('bin1.bin', 'wb') as file1:
        file1.write(data2)
    with open('bin2.bin', 'wb') as file2:
        file2.write(data1)

bin_files('bin1.bin', 'bin2.bin')





