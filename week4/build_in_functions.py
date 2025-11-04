
#####################################################

#ASCII Values

# print("Program Started!")
#
# letter = input("Please enter a standard character: ")
#
# if len(letter) == 1:
#     print(f"The ascii code for {letter} is {ord(letter)} ")
# else:
#     print("Error message")

print("Program Ended!")
########################################################

#ASCII Character

print("Program Started!")

ascii_code = int(input("Please enter an ASCII code: "))

if ascii_code in range(32,127):
        character = chr(ascii_code)
        print( print(f"The character represented by the ASCII code is {character}"))
else:
        print("Error! The number is not printable ASCII code.")

print("Program Ended!")

