#MAP
num = [1, 2, 3, 4, 5]

new_num = list(map(lambda x: x**3, num))
print(new_num)

#FILTER
number = [10, 11, 12, 13, 14]

print(list(filter(lambda x: x%2==0, number)))

#REDUCE
from functools import reduce

numbers = [1,2,3,4]
print(reduce(lambda x,y: x*y, numbers))