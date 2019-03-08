class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"HI, I am {self.name}")


john=Person("Jan Kowalski")

john.talk()

bob=Person("Bob Smith")

bob.talk()
