# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
# арифметическое всех чисел из отрезка [a;b], которые делятся на 3.


a = int(input())
b = int(input())
s = 0
t = 0
if a % 3 != 0:
    a = a + 3 - (a % 3)
for i in range(a, b + 1, 3):
    s += i
    t += 1
print(s / t)
