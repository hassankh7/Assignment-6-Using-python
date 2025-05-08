
# math_utils.py

class MathUtils:
    @staticmethod
    def add(a, b):
        """Returns the sum of a and b."""
        return a + b


# Example usage
if __name__ == "__main__":
    num1 = 12
    num2 = 8
    result = MathUtils.add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")