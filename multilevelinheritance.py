class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("the animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()