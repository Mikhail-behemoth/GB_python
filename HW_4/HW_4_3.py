# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = [2, 3, 3, 4, 5]

for j in range(0, len(list1)):
    k = list1[j]
    count = 0
    for i in range(0, len(list1)):
        if list1[i] == k:
            count = count + 1
    if count == 1:
        print (list1[j], end =' ')