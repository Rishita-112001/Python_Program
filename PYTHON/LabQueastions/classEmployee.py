class Person:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}")


class Employee(Person):
    def __init__(self, emp_id, name, dept, desg):
        super().__init__(emp_id, name)
        self.dept = dept
        self.desg = desg

    def display(self):
        super().display()
        print(f"Department: {self.dept}, Designation: {self.desg}")

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, dept, desg, sal):
        super().__init__(emp_id, name, dept, desg)
        self.sal = sal
        self.bonus = 0.2 * sal

    def calculate_salary(self):
        da = 0.1 * self.sal
        hra = 0.15 * self.sal
        pf = 0.08 * self.sal
        return self.sal + da + hra - pf

    def display(self):
        super().display()
        print(f"Salary: {self.sal}, Net Salary: {self.calculate_salary()}")

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, dept, desg, hrs_worked, hourly_charge):
        super().__init__(emp_id, name, dept, desg)
        self.hrs_worked = hrs_worked
        self.hourly_charge = hourly_charge

    def calculate_salary(self):
        return self.hrs_worked * self.hourly_charge

    def display(self):
        super().display()
        print(f"Hours Worked: {self.hrs_worked}, Hourly Charge: {self.hourly_charge}, Total Salary: {self.calculate_salary()}")

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def modify_salary(self, emp_id, new_salary):
        for emp in self.employees:
            if isinstance(emp, SalariedEmployee) and emp.emp_id == emp_id:
                emp.sal = new_salary
                return True
        return False

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.display()
                return
        print("Employee not found.")

    def calculate_salary(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"Calculated Salary: {emp.calculate_salary()}")
                return
        print("Employee not found.")

    def display_all(self):
        for emp in self.employees:
            emp.display()
            print("-" * 30)

ems = EmployeeManagementSystem()
ems.add_employee(SalariedEmployee(12, "Kishori", "Training", "Manager", 1111))
ems.add_employee(ContractEmployee(13, "Esha", "Insurance", "Manager", 12, 1000.00))

print("Displaying All Employees:")
ems.display_all()

print("Calculating Salary for ID 12:")
ems.calculate_salary(12)

print("Modifying Salary for ID 12:")
ems.modify_salary(12, 2000)

print("Displaying All Employees after Modification:")
ems.display_all()

print("Deleting Employee with ID 13:")
ems.delete_employee(13)

print("Displaying All Employees after Deletion:")
ems.display_all()
