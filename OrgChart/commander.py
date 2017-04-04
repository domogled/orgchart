
import cmd, sys


from datetime import date

class Command(cmd.Cmd):
    intro = 'Welcome to the orgchart shell.   Type help or ? to list commands.\n'
    prompt = 'orgchart: '
    file = None


    def __init__(self, orgchart_data, employees_data):
        
        # print(f'CREATE new Command({orgchart_data}, {employees_data})')
        
        self._departments = orgchart_data
        self._employees = employees_data
        
        super().__init__()
        

    def tree_departments(self, department_id):
        
        record = self._departments[department_id]

        yield record

        for child_id in record['children']:
            for subrecord in self.tree_departments(child_id):
                yield subrecord

    # ------------ COMMANDS do_* functions-------------- 

    def do_Department(self, args):
        '''
        Display the department name and the city for given department ID
        '''
        # assert len(args) == 2, f'Department expect one parameter, {len(args)} found'


        department = self.get_Department(args)

        print('{department_name}, {department_city}'.format(**department))
        

    def do_Count(self, args):
        '''
        Number of all employees for department INCLUDING all employees for department INCLUDING all its sub-departments (all levels, for example for Delivery it includes also Development, Python, Java) - for given department ID
        '''
        # assert len(args) == 2, f'Count expect one parameter, {len(args)} found'
        print(self.get_Count(args))

    def do_People(self, args):
        '''
        List of names of all employees for department INCLUDING all its sub-departments (all levels, for example for Delivery it includes also Development, Python, Java) - for given department ID
        '''
        # assert len(args) == 2, f'People expect one parameter, {len(args)} found'

        peoples = self.get_People(args)
        
        print(', '.join(peoples))

    def do_Avgage(self, args):
        '''
        Average age of all employees for department INCLUDING all its sub-departments (all levels, for example for Delivery it includes also Development, Python, Java) - for given department ID
        '''
        # assert len(args) == 2, f'Avgage expect one parameter, {len(args)} found'
        print(self.get_Avgage(args[0]))

    # ------------ COMMANDS get_* functions -------------- 

    def get_Department(self, department_id):
        
        return self._departments[department_id]
        

    def get_Count(self, department_id):
        
        count = 0

        for people in self._get_employees_in_departmens_tree(department_id):
            print(people)
            count = count + 1

        print('COUNT', count)
        return count

    def get_People(self, department_id):
        
        peoples = set()

        # peoples =  filter(lambda people: people['department_id'] in departments, self._employees.values())

        for people in self._get_employees_in_departmens_tree(department_id):
            # print('people_id', people, department_ids)
            peoples.add('{first_name} {surname}'.format(**people))

        return peoples


    def get_Avgage(self, department_id):
        
        ages = []

        current_date = date.today()

        for people in self._get_employees_in_departmens_tree(department_id):
            datum = people['birth_date']
            print(datum, current_date, current_date - datum)
            age = (current_date - datum) 
            ages.append(age.days / 365.25)


        print('AGES', ages)
        avg_ages = sum(ages, 0.0) / len(ages)
        print(avg_ages)
        exit()
        return avg_ages

        # ---- UTILS --------------

    def _get_employees_in_departmens_tree(self, root_department_id):
        
        department_ids = [ department['id'] for department in list(self.tree_departments(root_department_id))]
        
        for people_id, people in self._employees.items():
            
            if  people['department_id'] in department_ids:
                yield people

    # ------------ COMMANDS -------------- 

    # def postcmd(self, stop, line):
    #     print(f'postcmd {stop} {line}')