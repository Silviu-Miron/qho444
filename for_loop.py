


#Activity 1: Simple Loop

# mountains = int(input("How many mountains should I display?"))
#
# mountains_art = r"""
#    __
#   /  \_
#  /^    \
# /  ^    \_
# _/ ^ ^     ^\
# /  ^     ^    \
# """
#
# print("Displaying...")
# for i in range(mountains):
#     i+=1
#     print(mountains_art)
#
# print("Done!")


##################################################
# Activity 2: Count Down

# steps = int(input("How far are we from the target?\n"))
#
# for i in range(steps,0,-1):
#
#     print(f"{i} step remaining")


#################################################

#Activity 4 Characters

message = input("What word dou you see ?\n ")
index = 0

print("\n")
print("Displaying index positions...")
print("\n")

for letter in message:
    print(f" index {index}:, {letter}")
    index += 1

print("\n")
print("Done!")