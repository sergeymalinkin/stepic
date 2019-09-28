import requests

lines = 0
with open('C:/projects/stepic/week3/modules/dataset_3378_2.txt', 'r') as site:  # считываем ссылку из скаченного файла
    site = site.read() \
        .strip()
    filo = requests.get(site)  # GET запрос по полученой ранее ссылке
    for i in filo.text.splitlines():  # считаем строки в файле
        lines += 1
print(lines)
