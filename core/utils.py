import csv

from core.employee import Employee

DATABASE_FILE = "data.txt"
def read_database():
    employees = {}
    with open(DATABASE_FILE, 'r') as f:
        dict_reader = csv.DictReader(f)
        for item in dict_reader:
            name = item['name']
            item.pop('name')

            position = item["position"]
            monthly_salary = float(item["monthly_salary"])
            employees[name] = Employee(name, position, monthly_salary)

    return employees


def add_record_to_database(employee: Employee):
    with open(DATABASE_FILE, 'a') as f:
        f.write("\n")
        f.write(f"{employee.name},{employee.position},{str(employee.monthly_salary)}")




