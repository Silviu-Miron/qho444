from human import Human
from robot import Robot

class Planet:
def init(self, name):
self.name = name
self.inhabitants = []

def add(self, inhabitant):
    self.inhabitants.append(inhabitant)

def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)


def __repr__(self):
    humans = sum(isinstance(i, Human) for i in self.inhabitants)
    robots = sum(isinstance(i, Robot) for i in self.inhabitants)
    return (f"Planet(name={self.name},"
            f"Humans: {humans}, "
            f"Robots: {robots})")

def __str__(self):
    humans = sum(isinstance(i, Human) for i in self.inhabitants)
    robots = sum(isinstance(i, Robot) for i in self.inhabitants)
    return (f"Planet {self.name} | "
            f"Humans: {humans},"
            f"Robots: {robots}")





if name == "main":
earth = Planet("Earth")
h1 = Human()
h2 = Human()
r1 = Robot()
r2 = Robot()

earth.add(h1)
earth.add(h2)
earth.add(r1)
earth.add(r2)
print(earth)
print(repr(earth))