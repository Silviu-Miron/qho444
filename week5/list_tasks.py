# Activity 1 Simple List
###########################################################################
# def directions():
#     steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return steps
#
#
# def run_task1():
#     option = directions()
#     print(option)
#
#
# if __name__ == "__main__":
#     run_task1()


# #################################################################
# Activity 2:  Indexing


def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


# def run_task2():
#     print("Moving...")
#     direction = movement()
#     steps = [10, 5, 3, 1]
#
#     print(f"{direction [0] } for {steps[0]} steps ")
#     print(f"{direction [2] } for {steps[1]} steps ")
#     print(f"{direction [4] } for {steps[2]} steps ")
#     print(f"{direction [6] } for {steps[3]} steps ")
#
#
# if __name__ == "__main__":
#     run_task2()

##################################################################
# Activity 3: Iterate


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


directions()


def menu():
    # direct = input("Please enter a direction:")
    step_by_step = directions()
    print("\n")
    index = 0
    for index in range(len(step_by_step)):
        print(f"{index}: {step_by_step[index]}")
    index += 1


if __name__ == "__main__":
    menu()
#############################################################
# Activity 4:  Populate


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


directions()


def menu_and_input():
    print("Please select a direction:")
    direct = directions()
    index = 0
    for index in range(len(direct)):
        print(f"{index}: {direct[index]}")
        index += 1

    choice = int(input("Enter your choice: "))
    return direct[choice]


menu_and_input()


def run_task4():
    route = []
    print("Working out escape route...\n")

    # Collect 5 directions
    for _ in range(5):
        direction = menu_and_input()
        route.append(direction)

    print(f"\nEscape route: {route}")


# Run the program

if __name__ == "__main__":
    run_task4()
