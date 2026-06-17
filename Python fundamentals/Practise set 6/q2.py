class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print(f"This person is {self.name} and is {self.age} years old.")

p1 = Person("Alice", 24)
p1.displayInfo()