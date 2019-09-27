# Напишите программу, которая считывает список чисел lst из первой строки и число x из
# второй строки, которая выводит все позиции, на которых встречается число x в переданном
# списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке,
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
# Проверка:
# Sample Input 1: 5 8 2 7 8 8 2 4, 8 Sample Output 1:1 4 5
# Sample Input 2: 5 8 2 7 8 8 2 4, 10 Sample Output 2: Отсутствует

# Вариант 1
lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for i in range(0, len(lst)):
        if lst[i] == x:
            print(i, end=' ')

# Вариант 2
lst = [int(i) for i in input().split()]
x = int(input())
output = []
for i in range(0, len(lst)):
    if x == lst[i]:
        output.append(i)

if len(output) == 0:
    print('Отсутствует')
else:
    print(' '.join(str(i) for i in output))
