

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} car has started."
    
car1 = Car("Toyota")
print(car1.brand)
print(car1.start())