# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input("Введите размер списка: "))
list_num = list(range(-num, num+1)) 
import random
random.shuffle(list_num)
del list_num [num:]
print(list_num)

with open('file.txt') as file:
    x = int(file.readline())
    y = int(file.readline())

print(x, y)

pon = list_num[x]*list_num[y]
print (pon)