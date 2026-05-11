class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first+'.'+last+'@xyz.com').lower()
        Employee.num_of_emps +=1

    @classmethod
    def from_string(cls, empStr):
        first,last,pay = empStr.split(' ')
        return cls(first, last, pay)
    

emp1 = Employee('John', 'Smith', 50000)
print(emp1.email)

emp2 = Employee.from_string('Ramesh Das 790000')
print(emp2.__dict__)
