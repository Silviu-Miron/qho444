from human import Human
from robot import Robot

class Planet:
def init(self, name):
self.name = name
self.inhabitants = {
"humans": [],
"robots": []
}

def add_human(self, human):
    self.inhabitants["humans"].append(human)

def remove_human(self, human):
    self.inhabitants["humans"].remove(human)

def add_robot(self, robot):
    self.inhabitants["robots"].append(robot
                                      )
def remove_robot(self, robot):
    self.inhabitants["robots"].remove(robot)

def __repr__(self):
    return (f"Planet(name={self.name},"
            f"Humans: {len(self.inhabitants['humans'])}, "
            f"Robots: {len(self.inhabitants['robots'])})")

def __str__(self):
    return (f"Planet {self.name} | "
            f"Humans: {len(self.inhabitants['humans'])},"
            f"Robots: {len(self.inhabitants['robots'])}")
if name == "main":
earth = Planet("Earth")
h1 = Human()
h2 = Human()
r1 = Robot()
earth.add_human(h1)
earth.add_human(h2)
earth.add_robot(r1)
print(earth)
print(repr(earth))