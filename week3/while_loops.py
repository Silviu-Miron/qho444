
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

# bars = int(input(" How many bars should be charged?\n "))
#
# bar_numbers = 0
# while bar_numbers < bars:
#     print("Charging: █ ", end="")
#     print(" █ " * bar_numbers)
#     bar_numbers += 1
#
#
#
# print("\n")
# print("The battery is fully charged")


# Activity 4 : Repeating word

# message = input("Please enter a phase: ")
#
# word= "Hi"
# charged = ""
#
# while len(word) < len (message):
#     charged += word
#     print(charged[:len(message)])
# message = input("Please enter a phase: ")


# message = input("Please enter a phrase: \n")
#
# i = 0
# while i < len(message):
#     print(" Hi ", end="")
#     i +=1


# Activity 5 : Sum 100

# numbers =input("Calculating the sum of the first 100 numbers...")
#
# number = 0
# answer = 0
# while number < 100:
#     number +=1
#     answer += number
# print(f"...Done! The answer is {answer}")



#Activity 6 : Sum User Numbers

sum_numbers  = int(input("How many numbers should I sum up?"))

number =0
final = 0
while number < sum_numbers :
    number +=1
    repeat = int(input(f" Please enter number {number} of {sum_numbers}\n"))
    final += repeat
print(f"The answer is {final}")