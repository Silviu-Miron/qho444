"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
# Define welcome function
def show_welcome():
    print("_" * 40)
    print("     Disneyland Review Analysis System")
    print("_" * 40)
    print()


#Data set function
def load_dataset_message(count):
    print(f"Dataset loaded successfully. Total records are: {count}")
    print()


#Main menu function
def main_menu():
    print("Please enter one of the following options:\n")
    print("[A] View Date")
    print("[B] Visualize Date")
    print("[X] Exit\n")

    return get_choice("Enter your choice:",{"A","B","X"})



#Define Choice Function
def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().upper()
        print(f"You entered: {choice}")

        if choice in valid_choices:
            return choice

        print("Invalid Choice. Please try again.\n")



#Define submenu a function
def submenu_a():
    while True:
        print("\n Please Enter one of the following options:")
        print("[A] View reviews by Park")
        print("[B] Number of reviews by Park and reviews Locations")
        print("[C] Average Score per Year by Park")
        print("[D] Average score per park by review Location")
        print("[E] Go back to main menu\n")

        choice = get_choice("Enter your choice:",{"A","B","X","C","D","E"})

        if choice == "D":
            print("Returning to main menu...\n")
            return

        print(f"Option {choice} selected.")
        print("Feature will be implement later")




#Define submenu b function
def submenu_b():
    while True:
        print("\n Please Enter one of the following options:")
        print("[A] View reviews by Parks")
        print("[B] Park Ranking by Nationality")
        print("[C] Most popular Month by Park")
        print("[D] Go back to main menu\n")

        choice = get_choice("Enter your choice:",{"A","B","C","D","E"})

        if choice == "D":
            print("Returning to main menu...\n")
            return


    print(f"Option {choice} selected.")
    print("Feature will be implement later")



