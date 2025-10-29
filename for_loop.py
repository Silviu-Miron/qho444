


#Activity 1: Simple Loop

mountains = int(input("How many mountains should I display?"))

mountains_art = r"""
   __
  /  \_
 /^    \
/  ^    \_
_/ ^ ^     ^\
/  ^     ^    \
"""

print("Displaying...")
for i in range(mountains):
    i+=1
    print(mountains_art)

print("Done!")

