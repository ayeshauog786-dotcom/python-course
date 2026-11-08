from abc import ABC, abstractmethod

# __ ABSTRACT BASE CLASS (parent)
# Animal inherits from ABC
class Animals(ABC):

    # PARENT CONSTRUCTOR
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

        #concrete method
    def display(self):
            print(f"Name: {self.name}  |  Habitat: {self.habitat}")

            #abstarct method
    @abstractmethod
    def speak(self):
         pass
# child class 1
class Dog(Animals):

     def __init__(self, name, habitat, breed):
          super().__init__(name, habitat) 
          self.breed = breed

     def speak(self):
          print(f"{self.name} ({self.breed}) says: Woof! Woof!")


# child class 2
class Parrot(Animals):

     def __init__(self, name, habitat, phrase):
          super().__init__(name, habitat)
          self.phrase = phrase

     def speak(self):
          print(f"{self.name} says: {self.phrase}! {self.phrase}!")

#child class 3
class Lion(Animals):

     def __init__(self, name, habitat, pride):
          super().__init__(name, habitat)
          self.pride = pride

     def speak(self):
          print(f"{self.name} (Pride: {self.pride}) says : ROARRR!")

#CREATE OBJECTS AND RUN SHOW
Dog     = Dog("Bruno", "Home", "Labrador")
Parrot  =Parrot("Polly", "Jungle", "Squawk")
Lion    =Lion("Simba", "Savannah", "Pride Rock")

print("===  Animal Sound Show ===\n")
for animal in [Dog, Parrot, Lion]:
     animal.display()
     animal.speak()
     print()
             