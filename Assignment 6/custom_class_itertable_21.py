

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stops the iteration when below 0
        else:
            number = self.current
            self.current -= 1
            return number


# Test the Countdown class
start_number = int(input("Enter a starting number for countdown: "))

print("Countdown:")
for number in Countdown(start_number):
    print(number)