class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Some Sound")


class Dog(Animal):
    def sound(self):
        print("Barking...")


labra = Dog("Labra")
labra.sound()