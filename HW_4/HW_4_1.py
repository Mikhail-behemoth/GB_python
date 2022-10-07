# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

num = float(input("Введите число: "))
d = float(input("Задайте точность: "))

str_d = str(d)
k = len(str_d)-2

str_num = str(num)
lst_str = list(str_num)
for i in range(0, len(lst_str)):
    if lst_str[i] == '.':
        del lst_str[i+1+k:len(lst_str)]
        break

number = float(''.join(map(str, lst_str)))
print(number)