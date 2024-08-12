class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal is the parent o base class
# Mamal is the child or subclass
class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))  # True
print(isinstance(m, Animal))  # True
print(isinstance(m, object))  # True
o = object()

print(issubclass(Mammal, Animal))  # if a class derives from another class
print(issubclass(Mammal, object))  # if a class derives from another class
