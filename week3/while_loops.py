

# apple_removed = int(input("How many apples should I remove?\n"))
#
# total_apple = 0
# string = "Remove apple"
#
# while total_apple < apple_removed:
#     print(string)
#     total_apple +=1


# Task 2

#Create an input variable
obstacles = int(input("How many obstacles must avoid ?\n"))

#Define new variable
obstacles_number = 0

# while loop
while obstacles_number < obstacles:
    obstacles_number +=1
    print(f"Avoiding...Done!  {obstacles_number} obstacle avoided",end="")

#Printing final message
print("\n")
print("All obstacles have been avoided.")