def full_name(first, last):
    str = " ".join([first, last])
    return str

print(full_name("Royal", "Play"))


def calculate_length(length, width=10):
    return length*width

print(calculate_length(10,15))
print(calculate_length(10))