
#Activity 1 : Simple loop


# apple_removed = int(input("How many apples should I remove?\n"))
#
# total_apple = 0
# string = "Remove apple"
#
# while total_apple < apple_removed:
#     print(string)
#     total_apple +=1


# Activity 2 : Count

#Create an input variable
#obstacles = int(input("How many obstacles must avoid ?\n"))##

#Define new variable
#obstacles_number = 0

# while loop
#while obstacles_number < obstacles:
    #obstacles_number +=1
    #print(f"Avoiding...Done!  {obstacles_number} obstacle avoided",end="")

#Printing final message
# print("\n")
#print("All obstacles have been avoided.")


# Activity 3: ASCII

bars = int(input("How many bars should be charged?"))

bar_numbers = 0
while bar_numbers < bars:
    print("Charging: █" , end=" " )
    print(" █ "* bar_numbers)
    bar_numbers += 1



print("\n")
print("The battery is fully charged")