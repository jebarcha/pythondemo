class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


# Animal is the parent o base class
# Mamal is the child or subclass
class Mammal(Animal):
    def __init__(self):
        # super().__init__()
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
