


##########################################

#Activity 1

def display_ladder(steps):

   for _ in range(steps):
       print("""| |
                ***""")

def create_ladder():
    steps = int (input("How many steps would you like?"))
    display_ladder(steps)

create_ladder()



