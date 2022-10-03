# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите число: "))

a = list(range(0, num+1))
list1 = []

for i in range(0, num+1):
    if i == 0:
        a[i] = 0
    if i == 1:
        a[i] = i
    if i > 1:
        a[i] = -a[i-1] + a[i-2]
    list1.append(a[i])

del list1[0]
list1.reverse()

list2 = []
for i in range(0, num+1):
    if i == 0:
        a[i] = 0
    if i == 1:
        a[i] = i
    if i > 1:
        a[i] = a[i-1] + a[i-2]
    list2.append(a[i])

list3 = list1 + list2

print(list3)