# Create a class Employee with a private attribute _salary.

# Use @property to define a getter for salary.
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Warning: Salary cant be negative. Please try again!")
        else:
            self._salary =new_salary


new1 = Employee(60000)
print(new1.salary)

new1.salary = 50000
print(new1.salary)