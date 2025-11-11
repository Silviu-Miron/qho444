


##########################################

#Activity 1

# def display_ladder(steps):
#
#    for _ in range(steps):
#        print("""| |
#                 ***""")
#
# def create_ladder():
#     steps = int (input("How many steps would you like?"))
#     display_ladder(steps)
#
# create_ladder()



##########################################

#Activity 2 : Return Values

def sum_weights(char_weight, char_inventory):
    total =  char_weight + char_inventory
    return total


def calc_avg_weight(char_weight, char_inventory):
    total= sum_weights(char_weight, char_inventory)
    total/=2
    return total

def run():
    person_weight = float(input("What is the weight of the person?\n"))
    inventory_weight = float(input("What is the weight of the inventory?\n"))
    message = input("Please enter the word: sum or average ").lower()

    if message == "sum":
        total = sum_weights(person_weight, inventory_weight)
        print("The total is: ", total)
    elif message == "average":
        total = calc_avg_weight(person_weight, inventory_weight)
        print("The total is: ", total)
    else:
        print("Please enter a valid input.")


run()




##########################################

#Activity 4 : Return Values

# def manipulate_word():
#    word = input("Enter a word: ")
#    print("Choose one of the following options:")
#
#
#
#    option_1 = input("Display in a Box - display the word in an ASCII art box")
#    option_2 = input("Display Lower-case-display the word in lower-case e.g.hello")
#    option_3 = input("Display Upper-case-display the word in upper-case e.g.HELLO")
#    option_4 = input("Display Mirrored - display the word with its mirrored word e.g Hello | olleH")
#    option_5 = input("ask the user how many times you would like to display the word and then display "
#                     "the word that many times alternating between upper-case and lower-case")
#
#
#    print(option_1)
#    print(option_2)
#    print(option_3)
#    print(option_4)
#    print(option_5)
#
# manipulate_word()

# # Function 1: Display word in a box
# def display_in_box(word):
#     length = len(word)
#     print("*" * (length + 4))  # top border
#     print(f"* {word} *")       # word in middle
#     print("*" * (length + 4))  # bottom border
#
# # Function 2: Display word in lower-case
# def display_lowercase(word):
#     print(word.lower())
#
# # Function 3: Display word in upper-case
# def display_uppercase(word):
#     print(word.upper())
#
# # Function 4: Display mirrored word
# def display_mirrored(word):
#     mirrored = word[::-1]  # reverse the word
#     print(f"{word} | {mirrored}")
#
# # Function 5: Repeat word alternating between upper and lower case
# def repeat_word(word):
#     times = int(input("How many times would you like to repeat the word? "))
#     for i in range(times):
#         if i % 2 == 0:
#             print(word.upper())
#         else:
#             print(word.lower())
#
# # Function 6: Run the program
# def run_program():
#     # Ask the user for a word
#     word = input("Enter a word: ")
#
#     # Show the options
#     print("\nChoose an option:")
#     print("1) Display in a Box")
#     print("2) Display Lower-case")
#     print("3) Display Upper-case")
#     print("4) Display Mirrored")
#     print("5) Repeat")
#
#     # Get user choice
#     choice = input("Enter the option number (1-5): ")
#
#     # Execute the chosen function
#     if choice == "1":
#         display_in_box(word)
#     elif choice == "2":
#         display_lowercase(word)
#     elif choice == "3":
#         display_uppercase(word)
#     elif choice == "4":
#         display_mirrored(word)
#     elif choice == "5":
#         repeat_word(word)
#     else:
#         print("Invalid option. Please enter a number from 1 to 5.")
#
# # Run the program
# run_program()