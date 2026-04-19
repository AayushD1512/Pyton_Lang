def greet():
    print("Hello Python learner! Please enter a number for which squared result you want on the next line")

def square(num):    return num**2

greet()

num = int(input())
print(square(num))