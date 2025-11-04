

###########################################

#Activity 1 : Simple User Defined Function
# def listen ():
#     word = input("Enter a word: ")
#     print(f"That what a loud {word}")
#
# listen()

#############################################

#Activity 2 : Nesting

#Activity 1 : Simple User Defined Function
# def listen ():
#     word = input("Enter a word: ")
#     print(f"That what a loud {word}")
#
# listen()

# def adventure_game():
#     word = input("Enter a word representing what you see:")
#     if word.lower() == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine")
# adventure_game()


#############################################

#Activity 3 : Parameters


# def listen ():
#     word = input("Enter a word: ")
#     print(f"That what a loud {word}")
#
# listen()
#
# def adventure_game():
#     word = input("Enter a word representing what you see:")
#     if word.lower() == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine")
# adventure_game()
#
#
# def escape_play(plan):
#     if plan  ==  "jumping over":
#         print("We cannot escape that way! The boulder is too big!")
#     elif plan == "running around":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("That might just work! Let's go!")
#     else:
#         print("We cannot escape that way! The boulder is in the way!")
#
# escape_play("jumping over")
# escape_play("running around")
# escape_play("cross bridge ahead")


#############################################

#Activity 4 : LOOP

def cross_bridge (steps):
    distance = 0
    for distance in range(steps):
        print("Crossed step")
    if distance == 5:
        print("Bridge is collapsing!")

    if distance < 5 :
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)