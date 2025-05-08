

# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class lion:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}, who is a {self.breed}, is barking! Khao Khao!")

lion = lion("Mufasa","Simmba")
lion.bark()