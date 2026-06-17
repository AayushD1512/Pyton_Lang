class NegativeNumber(Exception):
    def __init__(self, message="Number should be positive integer only."):
        self.message = message
        super().__init__(self.message)


while True:
    try:
        # Input conversion is now safely inside the try block
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegativeNumber()
        print(5000 / num)
        break  # Exits the loop if everything succeeds

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    except ZeroDivisionError:
        print("Can't divide by zero. Try again.")

    except Exception as e:
        print("An unexpected error occurred:", e)
        break
