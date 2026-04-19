import my_util

def fib(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    
    return fib(n-2)+fib(n-1)

print(fib(7))

def safe_divide(a, b):
    if b == 0:
        return "B can't be 0"
    else:
        c = a/b
        return c
    
print(safe_divide(9,0))


print(my_util.isEven(8))