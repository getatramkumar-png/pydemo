import os
os.system("cls")
class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method using self as noraml way
    def display(self):
        print(self.name, self.salary)

    # Class method using cls , it refres class of the object
    @classmethod
    def change_company(cls, company):
        cls.company = company

    # Static method    nothing but notmal method, it does not require class object or constructor
    @staticmethod
    def calculate_bonus(salary):
        return salary * 10 / 100


emp=Employee("Ram","2k")

#when you try to chnage the class variable always use classmethod, insted of if you direclymodify the variable then it looks like the value is updated , but it actually creating one instacen variable and display theat variable only while you call obj.variablename


#emp.change_company("CTS")
emp.company="cts"
print(emp.company)
print(Employee.company)


Employee.calculate_bonus(100)
