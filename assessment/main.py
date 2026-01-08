"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

from assessment.tui import load_dataset_message, main_menu
from tui import show_welcome,get_choice,submenu_a,submenu_b
import csv

#Create function for load data set
def load_dataset():
    data =[]

    try:
        with open("data/disneyland_reviews.csv") as file:
            reader =csv.DictReader(file)
            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print("Error: Disneyland reviews  file not found.")
        exit()
    return data

#Define main function
def main():
    show_welcome()

    data = load_dataset()
    load_dataset_message(len(data))

#Use while loop for choosing options
    while True:
        choice = main_menu()

        if choice == "A":
            submenu_a()
        elif choice == "B":
            submenu_b()
        elif choice == "X":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







