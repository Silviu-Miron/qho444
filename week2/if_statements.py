

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
#
# citizen = False
# age = 18
#
# if citizen == True and age < 18:
#   print("You are not allow to vote")
# elif citizen == True and age >= 18:
#   print("You are allowed to vote")
# elif citizen == False and age < 18:
#   print("You are not a citizen and don't have the age to vote")
# elif citizen == False and age >= 18:
#   print("You are not a citizen, but you can vote ")
# else:
#   print("Invalid option ")



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
# odd_count += 1
#
# print(f"\n There were {even_count} even  and {odd_count} odd numbers.")


# first_number = 2
# second_number = 3
#
# if first_number > second_number:
#   print(f"{first_number} is greater than {second_number}")
# elif first_number < second_number:
#   print(f"{first_number} is less than {second_number}")
# else:
#   print("Choose one number")


# cover = input("What type of cover does the book have (soft or hard)? ").strip().lower()
# perfect = input("Is the book perfect bound (yes or no)? ").strip().lower()
#
# if cover == "soft":
#     message = "Soft cover books are easy to carry."
# elif cover == "hard":
#     message = "Hard cover books are durable and long-lasting."
# else:
#     message = "No recognized cover type — maybe your book is an ebook!"
#
# if perfect == "yes":
#     if cover == "soft":
#         message += " Soft cover perfect bound books are very popular!"
#     else:
#         message += " It is perfectly bound by the maker."
#
# print(message)
#
# location = input("where should I look").strip().lower()
#
# if location =="in the bedroom":
#     look = input("where in the bedroom should I look").strip().lower()
#     if look == "in the cupboard":
#         print("found some mess but no phone ")
#     else:
#         print("some mess but no phone in the cupboard, I am still looking")
# elif location =="in the bathroom":
#     look = input("where in the bathroom should I look").strip().lower()
#     if look == "in the bathtub":
#         print("Found a rubber duck but no phone ")
#     else:
#         print("found some shampoo and soap but not phone")
# elif location =="in the living room":
#     look = input("where in the living room should I look").strip().lower()
#     if look == "on the table":
#         print("yes, he/she found the phone")
#     else:
#         print("Congrats, you need a new phone")
# else:
#     print("I don't know where to keep the ruber ducky")