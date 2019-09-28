# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
# записана следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю
# оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
#
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому
# языку по всем абитуриентам.
#
# В качестве ответа на задание прикрепите полученный файл со средними оценками.
import re

with open('C:/projects/stepic/week3/io/3_4_3/dataset_3363_4.txt', 'r') as f:
    read_data = f.read()
    data = []
    data1 = []
    for i in read_data.split(";"):
        data += [i]

    for j in data:
        if re.search(r"\D", j) is not None:
            j = re.sub(r"\D", "", j)
        try:
            int(j)
            data1 += [j]
        except:
            pass
    print(data1)
    first, second, third = 0, 0, 0
    number_of_student = int((len(data1)) / 3)
    for i in range(number_of_student):
        first += int(data1[0 + 3 * int(i)])
        second += int(data1[1 + 3 * int(i)])
        third += int(data1[2 + 3 * int(i)])
        q = (int(data1[0 + 3 * int(i)]) + int(data1[1 + 3 * int(i)]) + int(data1[2 + 3 * int(i)])) / 3
        print(q)
    print(first / number_of_student, second / number_of_student, third / number_of_student)

    with open('C:/projects/stepic/week3/io/3_4_2/output.txt', 'w') as out:
        out.write(" ")
        out.write(str(number_of_student))