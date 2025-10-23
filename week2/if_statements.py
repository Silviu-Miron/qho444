

# Activity 1: If

# book_type = input("What type of book is this?\n")
#
# if  book_type.lower() == 'adventure':
#   print("I like adventure books!")
# print("Finished reading book")
#
#
# print(f"\n")
#
# activity = input("Please enter and activity: \n")


# Activity 2:IF ELSE

# if activity.lower() == 'calculate':
#   print("Performing Calculation...")
# else:
#   print("Performing activity...")
# print("Activity completed!")
# print("Activity completed!")

# Activity 3: IF ELIF

# directions = input("Towards which direction should I go (up,down, left or right)? \n")
#
# if directions == "up":
#   print("I am moving in an upward direction")
# elif directions == "down":
#   print("I am moving in an downward direction")
# elif directions == "left":
#   print("I am moving in an left direction")
# elif directions == "right":
#   print("I am moving in an right direction")
# else:
#   print("Choose one of the directions")


#Activity 4 : Modulo Operator

# whole_number = int(input("Please enter the whole number"))
#
# if whole_number % 2 != 0:
#   print(f"The number {whole_number} is an odd number. ")
# else:
#   print(f"The number {whole_number} is an even number. ")


#Activity 5 : Comparison Operators

# first_number = int(input(" Please enter the first number: "))
# second_number = int(input("Please enter the second number: "))
# if first_number > second_number:
#   print()
#   print("The second number is the smallest")
# else:
#   print("Add a number")

citizen = False
age = 18

if citizen == True and age < 18:
  print("You are not allow to vote")
elif citizen == True and age >= 18:
  print("You are allowed to vote")
elif citizen == False and age < 18:
  print("You are not a citizen and don't have the age to vote")
elif citizen == False and age >= 18:
  print("You are not a citizen, but you can vote ")
else:
  print("Invalid option ")



#Activity 6: Counter

#
# first_number =  int(input(" Please enter first number: \n"))
# second_number =  int(input(" Please enter second number: \n"))
# third_number =  int(input(" Please enter third number: \n"))
#
# even_count = 0
# odd_count = 0
# if first_number % 2 == 0:
#   even_count += 1
# else:
#   odd_count += 1
#
# if second_number % 2 == 0:
#   even_count += 1
# else:
#   odd_count += 1
#
# if third_number % 2 == 0:
#   even_count += 1
# else:
#   odd_count += 1
#
#   print(f"\n There were {even_count} even  and {odd_count} odd numbers.")
