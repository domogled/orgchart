#!/usr/bin/env python3


import click

from OrgChart.loader import load_departments, load_employees
from OrgChart import commander

@click.command()
@click.argument('orgchart_data_file', type=click.Path(exists=False))
@click.argument('employees_data_file', type=click.Path(exists=False))
def main(orgchart_data_file, employees_data_file):
    print(f'Load orgchart data from {orgchart_data_file}')

    orgchart_data = load_departments(orgchart_data_file)

    print(f'Load employees data from {employees_data_file}')

    employees_data = load_employees(employees_data_file)

    commander.Command(orgchart_data, employees_data).cmdloop(
                                                        # intro = '...'
                                                        )

if __name__ == '__main__':
    print('Welcome to orgchart')

    try:
        main()
    except Exception as err:
        print(err)
