# num = int(input("Enter a number for day of the week "))

# match num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input. Please enter a number between 1 and 7.")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of sum is: {result}")
    case "-":
        print(f"The result of sub is: {num1 - num2}")
    case "*":
        print(f"The result of mul is: {num1 * num2}")
    case "/":
        print(f"The result of div is: {num1 / num2}")
    case _:
        print("Invalid operation. Please enter one of +, -, *, /.")
        