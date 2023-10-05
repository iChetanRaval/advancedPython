class Employees1:
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept
        self.salary = salary

    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'Email is {self.email}')
        print(f'Department is {self.dept}')
        print(f'Salary is {self.salary}')

    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f'Department Change to {new_dept}')

emp1 = Employees1('Raju', 'Rajumm@gmail.com', 'Sales', 50000)
emp2 = Employees1('Chetan', 'chetanraval@gmail.com', 'Engineer', 60000)
emp1.emp_info()
emp2.emp_info()
emp2.change_dept("Google DEvloper")
print(emp1.name)
