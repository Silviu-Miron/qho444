


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