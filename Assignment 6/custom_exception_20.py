

# Step 1: Custom Exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)


# Step 2: Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print("Age is valid. Access granted.")


# Step 3: Using try...except to handle exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number")