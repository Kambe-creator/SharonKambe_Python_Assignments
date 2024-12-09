from abc import ABC, abstractmethod  # For abstract base classes

# Abstract Base Class (Enforces move method)
class Mover(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sound(self):
        pass

# Animal classes
class Dog(Mover):
    def move(self):
        return "The dog runs on four legs. 🐕"
    
    def sound(self):
        return "The dog barks. Woof woof!"

class Bird(Mover):
    def move(self):
        return "The bird flies through the sky. 🐦"
    
    def sound(self):
        return "The bird chirps. Tweet tweet!"

class Fish(Mover):
    def move(self):
        return "The fish swims in the water. 🐟"
    
    def sound(self):
        return "The fish is silent. 🤫"

# Vehicle classes
class Car(Mover):
    def move(self):
        return "The car drives on the road. 🚗"
    
    def sound(self):
        return "The car honks. Beep beep!"

class Plane(Mover):
    def move(self):
        return "The plane flies through the clouds. ✈️"
    
    def sound(self):
        return "The plane roars. Vroooom!"

class Boat(Mover):
    def move(self):
        return "The boat sails on water. 🚤"
    
    def sound(self):
        return "The boat hums. Mmmmmm."

# Additional classes
class Horse(Mover):
    def move(self):
        return "The horse gallops across the field. 🐎"
    
    def sound(self):
        return "The horse neighs. Neighhh!"

class Train(Mover):
    def move(self):
        return "The train runs on rails. 🚆"
    
    def sound(self):
        return "The train whistles. Choo choo!"

# Demonstration function
def demonstrate_actions():
    movers = [Dog(), Bird(), Fish(), Car(), Plane(), Boat(), Horse(), Train()]
    
    for mover in movers:
        print(mover.move())
        print(mover.sound())
        print("-" * 40)

# Execute the function
if __name__ == "__main__":
    demonstrate_actions()
