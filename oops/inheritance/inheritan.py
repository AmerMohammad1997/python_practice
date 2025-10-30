class Animal:
    def speak(self):
        print("Animl Speaks")
    
class Dog(Animal):
    def speak(self):
        return super().speak()
dog = Dog()
dog.speak()