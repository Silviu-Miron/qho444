


class Human:
    MAX_ENERGY = 100
    def __init__(self):
        self.energy = Human.MAX_ENERGY
        self.name = "Human"
        self.age=0

    def display(self):
        print(f"I am {self.name}")




human = Human()
human.display()







