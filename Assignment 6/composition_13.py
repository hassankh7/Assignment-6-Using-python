

# Engine class
class Engine:
    def start(self):
        return "Engine started!"


# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # composition: Engine object inside Car

    def start_car(self):
        return self.engine.start()  # accessing Engine's method


# Creating Engine object
engine1 = Engine()

# Passing Engine object to Car
my_car = Car(engine1)

# Starting the car via Engine's method
print(my_car.start_car())