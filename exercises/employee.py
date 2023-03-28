"""
A database for employees at a company

Data:


APIs:

"""

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.employees = [[self.emp_id, self.emp_name, self.emp_salary, self.emp_department]]
    def get_employees(self):
        for employee in self.employees:
            print(employee)

    def get_employee_by_id(self, id):
        for employee in self.employees:
            if employee[0] == id:
                return employee

    def add_employee(self, emp_id, emp_name, emp_salary, emp_department):
        self.employees.append([emp_id, emp_name, emp_salary, emp_department])

    def emp_assign_department(self, emp_id, emp_department):
        employee = self.get_employee_by_id(emp_id)
        employee[3] = emp_department

    def get_salary_by_id(self, id):
        for employee in self.employees:
            if employee[0] == id:
                return employee[2]

    def calculate_employee_overtime(self, emp_id, hours_worked):
        overtime = hours_worked - 50
        overtime = (overtime*self.get_salary_by_id(emp_id))/50
        return overtime


emp_data = Employee(1, "Rebecca", 12, "ACCOUNTING")
emp_data.add_employee(2, "Carlos", 12, "ENGINEERING")
emp_data.emp_assign_department(2, "HR")

emp_data.get_employees()
print(emp_data.calculate_employee_overtime(2, 70))

