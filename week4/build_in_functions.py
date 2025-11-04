print("Program Started!")

letter = input("Please enter a standard character: ")

if len(letter) == 1:
    print(f"The ascii code for {letter} is {ord(letter)} ")
else:
    print("Error message")