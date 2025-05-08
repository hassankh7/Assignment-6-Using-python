

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected (by convention)
        self.__ssn = ssn         # Private

# Create object
emp = Employee("Hassan", 50000, "123-45-6789")

# Access public variable
print("Public (name):", emp.name)  # ✅ Accessible

# Access protected variable
print("Protected (_salary):", emp._salary)  # ✅ Accessible but not recommended

# Access private variable directly
try:
    print("Private (__ssn):", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError:
    print("Private (__ssn): Cannot access directly!")

# Correct way to access private variable (optional)
print("Private (__ssn) via name mangling:", emp._Employee__ssn)
