

###########################################

#Activity 1 : Simple User Defined Function
# def listen ():
#     word = input("Enter a word: ")
#     print(f"That what a loud {word}")
#
# listen()

#############################################

#Activity 2 : Nesting

def adventure_game():
    word = input("Enter a word representing what you see:")
    if word.lower() == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine")
adventure_game()