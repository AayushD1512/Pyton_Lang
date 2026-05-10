class Employee:
    emp_count= 0
    pay_raise = 1.04

    def __init__ (self, name, pay):
        self.name = name
        self.pay = pay
        Employee.emp_count += 1

    # def content(self):
    #     return f'{self.name} earms {self.pay} dollars'

    def raise_pay(self):
        self.pay = int(self.pay * self.pay_raise) # if we write Emplyee.pay_raise then main class value will considered, for self.pay_raise then set value will considered.
    
emp1= Employee('John', 50000)
emp2 = Employee('Mrinal', 60000)

emp1.pay_raise = 1.1
emp1.raise_pay()

print(emp1.pay)
