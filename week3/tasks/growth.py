# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов. Напишите программу,
# которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося. Файл состоит из набора строк,
# каждая из которых представляет собой три поля: Класс Фамилия Рост Класс обозначается только числом. Буквенные
# модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве
# роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного
# числа.

setClasses = tuple(str(i) for i in range(1, 12))
dictHeight = dict.fromkeys(setClasses, 0)
dictCount = dict.fromkeys(setClasses, 0)

with open('C:/projects/stepic/week3/tasks/dataset_3380_5.txt', encoding='UTF-8') as inf:
    for line in inf:
        lst = line.strip().split('\t')
        dictHeight[lst[0]] += float(lst[2])
        dictCount[lst[0]] += 1

for i in setClasses:
    if dictHeight[i] == 0:
        d = '-'
    else:
        d = str(dictHeight[i] / dictCount[i])
    print(i + ' ' + d)