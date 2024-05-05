'''
a) Sa se scrie o functie care citeste datele din fisierul `employees.json`.

b) Sa se creeze o functie care afiseaza toti angajatii care au mai putin de 5 zile de concediu medicalc) Sa se scrie in fisierul employees_less_than_{salar}.json toti angajatii care au un salar mai mic decat un numar dat. Numele fisierului depinde de valoarea dupa care se filtreaza.
'''

import json
from pprint import pprint


def read(filename):
    with open(filename,'r') as f:
        return json.load(f)

pprint(read('employees.json'))

def read_filtered(filename):
    data=read(filename)
    for employee in data :
        if employee['sick_days_remaining'] <10:
            print(employee['name'])
read_filtered('employees.json')

'''

c) Sa se scrie in fisierul employees_less_than_{salar}.json toti angajatii care au un salar mai mic decat un numar dat. Numele fisierului depinde de valoarea dupa care se filtreaza.

'''

def write_filter(filename, max_salary):
    data = read(filename)
    employees = []
    for employee in data:
        if employee['salary'] < max_salary:
            employees.append(employee)
    with open(f'employees_less_than_{max_salary}.json', 'w') as f:
        json.dump(employees, f, indent=2)


write_filter('employees.json', 80000)

