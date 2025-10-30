from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Marutii(Car):
    def start_engine(self):
        print("car engine started")

car = Marutii()
car.start_engine()