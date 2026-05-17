class Employee:
    countEmployee = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first+'.'+last+'@vscode.com').lower()
        Employee.countEmployee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

class Developer(Employee):
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang


class Manager(Employee):
    def __init__(self, first, last, pay, emp = None):
        super().__init__(first, last, pay)

        if emp is None:
            self.emp = []
        else:
            self.emp = emp

    
    def addEmp(self, employee):
        if employee not in self.emp:
            self.emp.append(employee)

    def removeEmp(self, employee):
        if employee in self.emp:
            self.emp.remove(employee)
    
    def printEmp(self):
        for employee in self.emp:
            print('--->', employee.fullname())


dev1 = Developer('Corey', 'Chase', 89000, 'Python')
dev2 = Developer('Brandon', 'Cooper', 990000, 'Java')
dev3 = Developer('Test', 'User', 89000, 'C++')

print(dev1.fullname())

mngr1 = Manager('Sue', 'Johnson', 100000, [dev1, dev2])

mngr1.addEmp(dev3)
mngr1.removeEmp(dev1)
mngr1.printEmp()