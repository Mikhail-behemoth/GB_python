# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehensio

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input("Введите номер четверти:\n"))

a = lambda x: "X > 0; Y > 0" if x == 1 else ("X < 0; Y > 0" if x == 2 else ("X < 0; Y < 0" if x == 3 else ("X > 0; Y < 0" if x == 4 else "Такого номера четверти нет")))

print(a(num))