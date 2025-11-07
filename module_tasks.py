# importing modules
import random
from random import randrange

# define variables
minimum_value = int(input("Please enter the minimum value: \n"))
maximum_value = int(input("Please enter the maximum value:\n "))
number = int(input("I am thinking of a number between 1 and 10 . Can you guess what it is?\n"))

result = (randrange(minimum_value, maximum_value))
print(result)

# create logic for
if result > number:
    print("You guessed too low")
    print("Try again")
    print(result)
elif result < number:
    print("You guessed too high")
    print("Try again")
    print(result)
elif result == number:
    print("Congratulations! You guessed my number!")
    print(result)
else:
    print("Sorry, you didn't guess the number")

