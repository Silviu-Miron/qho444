from babel.messages.jslexer import name_re


class Inhabitant:
    MAX_ENERGY = 10

    def __init__(self,name="Inhabitant", age =0,energy = MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = max(0,min(energy,Inhabitant.MAX_ENERGY))

    def grow(self):
        self.age+=1


    def eat(self,amount):
        self.energy = min(self.energy+amount,Inhabitant.MAX_ENERGY)


    def move (self,distance):
        self.energy=max(self.energy -distance,0)


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


    def __str__(self):
        return f"{self.name}(Age:{self.age}, Energy:{self.energy})"






