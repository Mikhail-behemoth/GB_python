# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print("Введите число ")
num = int(input())

list = []
for i in range(1, num+1):
    a = (1 + 1 / i)**i
    list.append(a)

print(format(sum(list), '.2f'))