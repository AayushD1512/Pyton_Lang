
class Employee:
    raise_amount = 1.04
    empCount = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first+'.'+last+'@newCompany.com').lower()
        Employee.empCount += 1

    def fullname(self):
        return ('{} {}'.format(self.first, self.last)).upper()

    def getRaise(self):
        self.pay *= self.raise_amount

    @classmethod
    def fromString(cls, empStr):
        first,last,pay = empStr.split(' ')
        return cls(first,last,pay)
    
class Developer(Employee):
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def addEmp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def removeEmp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def printEmployee(self):
        if not self.employee:
            print('No Employee managed by the Manager')
        else:
            for emp in self.employee:
                print('---->',emp.fullname())


dev1 = Developer('Corey', 'Chase', 89000, 'Java')
dev2 = Developer('Brian', 'Cooper', 99000, 'JavaScript')
dev3 = Developer('Test', 'User', 89000, 'Python')

mg1 = Manager('sue', 'Johnson', 100000, [dev1, dev2])
# mg1.printEmployee()
mg1.addEmp(dev3)
mg1.removeEmp(dev1)
mg1.printEmployee()