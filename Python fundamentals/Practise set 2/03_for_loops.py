# for i in range(1, 11):
#     print(i)

# num = int(input("Enter a number of multiplication table"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# num = 0
# for i in range (1,101):
#     num += i

# print(f"The sum is: {num}")


# for i in range(5):
#     for j in range(1, i+1):
#         print(f"* ", end="") # end="" is used to print the stars in the same line otherwise it will print in new line
#     print()


# i = 1
# while i<=10:
#     print(i, end=" ")
#     i += 1

# password = "hiraki"
# text = input("Enter the password: ")
# text = text.lower() # Convert the input to lowercase to make the password case-insensitive
# while text != password:
#     print("Incorrect password. Try again.")
#     text = input("Enter the password: ")
# print("Correct password. Access granted.")

num = 123
rev = 0
while num > 0:
    rem = num%10
    rev =rev*10 + rem
    num = num//10
print(f"The reversed number is: {rev}")

