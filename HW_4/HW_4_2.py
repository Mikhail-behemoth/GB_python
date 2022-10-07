# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите натуральное число: "))

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(f'{n:.{0}f}'))
   return primfac

print (primfacs(n))