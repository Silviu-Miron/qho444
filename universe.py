import random
import matplotlib.pyplot as plt
from planet import Planet
from human import Human
from robot import Robot

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self):
        planet = Planet(f"Planet - {len(self.planets) + 1}")

        # Add humans
        for _ in range(random.randint(1, 5)):
            planet.add(Human())

        # Add robots
        for _ in range(random.randint(1, 5)):
            planet.add(Robot())

        self.planets.append(planet)

    def show_populations(self, selection):
        names = [p.name for p in self.planets]

        human_counts = []
        robot_counts = []
        total_counts = []

        for p in self.planets:
            humans = sum(1 for i in p.inhabitants if isinstance(i, Human))
            robots = sum(1 for i in p.inhabitants if isinstance(i, Robot))
            total = humans + robots

            human_counts.append(humans)
            robot_counts.append(robots)
            total_counts.append(total)

        if selection == "human":
            values = human_counts
            label = "Human Population"
        elif selection == "robot":
            values = robot_counts
            label = "Robot Population"
        else:
            values = total_counts
            label = "Total Population"

        plt.bar(names, values)
        plt.ylabel(label)
        plt.xlabel("Planets")
        plt.title(label + " Per Planet")
        plt.show()


if __name__ == "__main__":
    universe = Universe()
    for _ in range(3):
        universe.generate()
    universe.show_populations("both")