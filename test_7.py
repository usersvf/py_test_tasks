from random import randint
from random import choice
from string import ascii_letters
from timeit import default_timer
import csv

letters = ascii_letters
csv_values = []

def generate_csv(N: int, header: dict):
    start = default_timer()
    csv_values.append([head for head in header.keys()])

    for row in range(1, N):
        row_list = [] 
        for type in header.values():
            if type == 'str':
                row_list.append(''.join(choice(letters) for i in range(randint(1, 100))))
            if type == 'int':
                row_list.append(randint(0, 100))
            if type == 'bool':
                row_list.append(choice([True, False]))
        
        csv_values.append(row_list)

    out_csv = csv.writer(open('random_generated.csv','w', newline=''), delimiter=',')
    out_csv.writerows(csv_values)

    end = default_timer()

    return print(
        f'Сгенирован {'random_generated.csv'}, количество строк: {N}, заголовки: {[head for head in header.keys()]} с типами значений в колонках {[type for type in header.values()]}. Время генерации: {end - start:.2f} cекунд'
                )


#tests

headers = {'first_name': 'str', 'last_name': 'str', 'age': 'int', 'is_client': 'bool', 'address': 'str', 'is_valid': 'bool'}
generate_csv(300000, headers)