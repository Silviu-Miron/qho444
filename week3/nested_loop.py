

#################################################

#Activity 1

# rows = int(input("How many rows would you like ?\n"))
#
# columns = int(input("How many columns would you like ?\n"))
#
#
# for row in range(rows):
#     for column in range (columns):
#         print(":-)",end="")
#     print()


#################################################

#Activity 2 Nesting

character = input("Enter a sequence of characters consisting of dashes and two markers \n")

marker = input("Enter a character representing a marker \n")

for character in character:
    print(character, end="")
    for marker in marker:
        print(marker, end="")
print(character)