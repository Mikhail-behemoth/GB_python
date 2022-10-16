# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehensio

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]

b = list(map(lambda x: x-int(x), a))

c = [i for i in b if i != 0]

max = c[0]
min = c[0]

for i in range(1, len(c)):
    if b[i] > max:
        max = b[i]
    if b[i] < min:
        min = b[i]

print(format(max-min, '.2f'))