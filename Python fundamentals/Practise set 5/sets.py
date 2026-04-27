my_set = {1, 2, 3, 3, 4}
print(my_set)

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

#check if 4 is in the set
print(4 in my_set)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))