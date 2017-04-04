import csv

from datetime import date

def load_departments(source_file):

    with open(source_file, newline='', encoding='utf-8') as csvfile:

        data = csv.reader(csvfile, delimiter=';', quotechar='|')
        # data = csv.DictReader(csvfile)

        def load_record(record):

            id, parent, department_name, department_city = record

            return {
                'id': int(id),
                'parent_id': int(parent) if parent else None,
                'department_name': department_name,
                'department_city': department_city,
                'children': []
            }

        data = {record['id']: record for record in map(load_record, data)}

        for id, record in data.items():
            parent_id = record['parent_id']
            if parent_id is not None:
                parent = data[parent_id]
                parent['children'].append(id)

        # print('DATA', data)
        return data

def load_employees(source_file):
    
    with open(source_file, newline='', encoding='utf-8') as csvfile:

        data = csv.reader(csvfile, delimiter=';', quotechar='|')
        # data = csv.DictReader(csvfile)

        def load_record(record):
    
            id, first_name, surname, department_id, birth_date = record

            return {
                'id': int(id),
                'first_name': first_name,
                'surname': surname,
                'department_id': int(department_id),
                'birth_date': parse_date(birth_date)
            }

        data = {record[0]: load_record(record) for record in data }
        # print('DATA', data)
        return data


def parse_date(_date):
    
    day, month, year = map(int, _date.split('.'))
    return date(year, month, day)