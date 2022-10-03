# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите число '))
if num < 0:
    num = -num
str_num = str(num)
str_num = str_num.replace('.', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
s = sum(lst_num)
print (s)