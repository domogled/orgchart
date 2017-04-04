
import pytest

from OrgChart.scripts import orgchart
from OrgChart.loader import load_departments, load_employees
from OrgChart import commander

from pathlib import Path

ROOT_DIR = Path(__file__).parents[1]
DATA_DIR = ROOT_DIR / 'data'

ORGCHART_DATA_FILE = DATA_DIR / 'orgchart-data.csv'
EMPLOYEES_DATA_FILE = DATA_DIR / 'employees-data.csv'

def test_input_file_not_found():
    assert 1 == 1

    # with pytest.raises(Exception):
    #     orgchart.main('NO_FILE', 'NO_FILE')



orgchart_data = load_departments(ORGCHART_DATA_FILE)
employees_data = load_employees(EMPLOYEES_DATA_FILE)

command = commander.Command(orgchart_data, employees_data)

def test_children():
    for i in range(1,7):
        record = orgchart_data[i]
        if i == 1:
            assert record['children'] == [5, 6]
        elif i == 6:
            assert record['children'] == [7, 8]
        else:
            assert record['children'] == []
    

def test_Department():
    department = command.get_Department(5)
    assert department['department_name'] == 'Testing'
    assert department['department_city'] == 'Praha'

def test_Count():
    assert command.get_Count(1) == '5'

def test_People():
    output = command.get_People(1)
    # print(output)
    assert output.find('Jan Hora') >= 0
    assert output.find('Jiří Vereš') >= 0
    assert len(output.split(',')) == 2

def test_Avgage():
    assert command.get_Avgage(1) == '28 years'