
# TODO

class Robot:
   MAX_ENERGY = 100
   laws = "Protect, Obey and Survive"

    @staticmethod
    def the_laws():
      print(Robot.laws)

    @classmethod
    def assemble(cls):
     return cls("Assembled Robot")

   def __init__(self, name="Robot"):
    self.name = name
    self.age = 0
    self.energy = 0

  def display(self):
    print(f"I am {self.name}")

robot = Robot()
robot.display()



