# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке, и после первого введенного нуля выводит
# сумму полученных на вход чисел.
s = 0
x = int(input())
s += x
while x != 0:
    x = int(input())
    s += x
print(s)