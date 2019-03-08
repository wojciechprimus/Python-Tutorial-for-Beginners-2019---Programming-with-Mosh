class Animals:
    def walk(self):
        print("walk")

class Dog(Animals):
    def bark(self):
        print("bark")


class Cat(Animals):
    pass

dog1=Dog()
dog1.walk()
