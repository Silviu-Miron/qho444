import random
import matplotlib.pyplot as plt
from planet import Planet
from human import Human
from robot import Robot

class Universe:
def init(self):
self.planets = []

def generate(self):
    planet = Planet(f"Plannet - {len(self.planets)+1}")

    for _ in range(random.randint(1, 5)):
        planet.add_human(Human())

    for _ in range(random.randint(1, 5)):
        planet.add_robot(Robot())

    self.planets.append(planet)

def show_populations(self, selection):
    names = [p.name for p in self.planets]

    if selection == "human":
        values = [len(p.inhabitants["humans"]) for p in self.planets]
        label = "Human Population"
    elif selection == "robot":
        values = [len(p.inhabitants["robots"]) for p in self.planets]
        label = "Robot Population"
    else:
        values = [
            len(p.inhabitants["humans"]) + len(p.inhabitants["robots"])
                  for p in self.planets
        ]
        label = "Total Population"

    plt.bar(names, values)
    plt.ylabel(label)
    plt.xlabel("Planets")
    plt.title(label + "Per Plannet")
    plt.show()
if name == "main":
universe = Universe()
for _ in range(3):
universe.generate()
universe.show_populations("both")