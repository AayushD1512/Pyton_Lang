def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper


@logger
def sayHello():
    print("Hello")

sayHello()


# Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

import time

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

@timer
def sumOfNumbers():
    total = 0
    for i in range(1, 1000001):
        total+= i

sumOfNumbers()