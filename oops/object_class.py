class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
    def driving(self):
        print(f"This is {self.brand} car model: {self.model}" )

my_car = Car(brand="Toyot",model="2021")
my_car.driving()