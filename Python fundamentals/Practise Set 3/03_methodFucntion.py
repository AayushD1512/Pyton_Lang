s = " i love python programming "
count = 0
print(s.strip())

print(s.title())

# print(s.find("o"))
for char in s:
    if char == 'o':
        count += 1

print(f"number of o is {count}")
print(s.isalnum())