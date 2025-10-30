class Animal:
    def sound(self):
        print("Some genericc sound")
class Dog(Animal):
    def sound(self):
        print("Makes Woof Sound")

class Cat(Animal):
    def sound(self):
        print("Meow Mewo")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())
make_sound(Animal())