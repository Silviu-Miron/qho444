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
# run_task1()


# #################################################################
# Activity 2:  Indexing


# def movement():
#     path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
#     return path

#
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
# run_task2()
##################################################################
# Activity 3: Iterate


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu():
    print("Please select the direction:")
    step_by_step = directions()
    print("\n")
    index = 0
    for index in range(len(step_by_step)):
        print(f"{index}: {step_by_step[index]}")
    index += 1


menu()
