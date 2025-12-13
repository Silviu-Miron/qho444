from matplotlib import pyplot as plt
import random


# import matplotlib.pyplot as plt
#
# def display_line(x_values, y_values):
#     plt.plot(x_values, y_values)
#     plt.xlabel("X Values")
#     plt.ylabel("Y Values")
#     plt.title("Simple line plot")
#     plt.show()
#
#
# def run_task1():
#     x_values = [1, 2, 3, 4, 5]
#     y_values = [1, 4, 9, 16, 25]
#     display_line(x_values, y_values)
#
# run_task1()


#Activeity 2
#
# def small():
#     x = [1,1,2,2,1]
#     y=[1,2,2,1,1]
#     plt.plot(x,y,'ro:')
#
# def medium():
#     x = [0,0,3,3,0]
#     y=[0,3,3,0,0]
#     plt.plot(x,y,'gs--')
#
# def large():
#     x = [-1,-1,4,4,-1]
#     y=[-1,4,4,-1,-1]
#     plt.plot(x,y,'bp-')
#
# plt.figure()
# small()
# medium()
# large()
# plt.title("Nested square")
# plt.show()

#Activity 3

# def coordinate ():
#     x = float(input("Enter the x values: "))
#     y = float(input("Enter the y values: "))
#     return x,y
#
# def path():
#     print("Retrieving path")
#     x_values = []
#     y_values = []
#
#     for _ in range(4):
#         data = coordinate()
#         x_values.append(data[0])
#         y_values.append(data[1])
#
#     return [x_values,y_values]
#
# def run_task3():
#     values = path()
#     plt.plot(values[0],values[1],'ro--')
#     plt.xlabel('X Axis')
#     plt.ylabel('Y Axis')
#     plt.title('User pash plot')
#     plt.show()
#
#
#
# if __name__ == "__main__":
#     run_task3()

#Activity 4

def data():
    paths = {}

    paths["lines"] =input("Choose your line style (:, --, -")
    paths["color"]=input ("Choose your color (r, g, b)")
    paths["marker"]=input("Choose your marker (o,s, ^)")

    return paths

def generate():
    print("How many lines would you like to display?")
    n = int(input())

    for _ in range(n):
        values = data()

        x = random.sample(range(1, 21), 5)
        y = random.sample(range(1, 21), 5)

        style = values["color"] + values["marker"] + values["lines"]
        plt.plot(x,y, style)
        plt.title("User - generated Style")
        plt.show()


def run ():
    print("Running...")
    generate()
    print("Done!")

run()



