from matplotlib import pyplot as plt


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

def small():
    x = [1,1,2,2,1]
    y=[1,2,2,1,1]
    plt.plot(x,y,'ro:')

def medium():
    x = [0,0,3,3,0]
    y=[0,3,3,0,0]
    plt.plot(x,y,'gs--')

def large():
    x = [-1,-1,4,4,-1]
    y=[-1,4,4,-1,-1]
    plt.plot(x,y,'bp-')

plt.figure()
small()
medium()
large()
plt.title("Nested square")
plt.show()


