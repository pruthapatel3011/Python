from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("the car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motocycle")

    def stop(self):
        print("the motorcycle is stopped")

#vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()