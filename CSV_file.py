# csv = comma separated values

import csv
from pprint import pprint

from tabulate import tabulate


def read(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)  # acest reader este iterator peste toate liniile din fisierul 'f' si returneaza
        return list(reader)


angajati = read('angajati.csv')
print(angajati)
tabel = tabulate(angajati[1:], headers=angajati[0])
tabel2 = tabulate(angajati, headers=angajati[0])
print(tabel)
print(tabel2)


def write(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)

        writer.writerows(data)


data = [
    ["Nume", "Varsta"],
    ["Sergiu", "25"],
    ["Andrei", "30"],
    ["Cristi", "34"]
]

write('persoane.csv', data)


def read_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


pprint(read_dict('angajati.csv'))


def write_dict(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


data2 = [
    {"Nume": "Sergiu", "Varsta": "25"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}

]
write_dict('persoane2.csv', data2)
