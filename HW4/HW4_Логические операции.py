# Логические операции:
# 1 Присвойте двум переменным любые числовые значения.
# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
# 3 Аналогично выполните п. 2, но уже используя оператор or.
# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.

a = 5
b = 10

expression1 = (a < b) and (b == 10)
expression2 = (a > 0) and (b > 5)
expression3 = (a > b) and (b > 5)
expression4 = (a == 5) and (b < 5)

print(expression1, expression2, expression3, expression4)

expression5 = (a > b) or (b == 5)
expression6 = (a > 14) or (b > 15)
expression7 = (a > b) or (b > 5)
expression8 = (a == 5) or (b < 5)

print(expression5, expression6, expression7, expression8)

str1 = "hello"
str2 = "world"

print(str1 == 'hello' and str2 == 'world')
print(str1 != 'world' and len(str2) == 5)
print(str1 == 'hi' and len(str2) == 5)
print(str1 == 'hello' and len(str2) == 10)