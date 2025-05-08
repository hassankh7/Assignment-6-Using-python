
# Create a class Person with a constructor that sets the name.

class Person:
    def __init__(self,name):
        self.name = name
        print("Person Object created with name",self.name)


class Teacher(Person):
        def __init__(self, name,subject):
             super().__init__(name)
             self.subject = subject
             print("Teacher teaches" ,self.subject)

person_obj = Person("Hassan")
teacher_obj = Teacher("Hassan","Python")