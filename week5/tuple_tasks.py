#########################################################
# Activity 1 : Simple Tuple

# temperature = (19, 23, 21, 20, 18, 22)
#
# # Concatenate tuple (this creates a new tuple)
# all_temperatures = temperature + (20, 21)
# print(all_temperatures)
#
#
# # Repeat a tuple
#
# print(temperature * 2)
#
# # Check membership of a tuple
# print(20 in temperature)
#
#
# print(f"The lowest temperature is: {min(temperature)}")
# print(f"The highest temperature is: {max(temperature)}")


def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods


def run_task1():
    hood = likelihood()
    print(f"Minimum likelihood of falling: {min(hood)}% ")


run_task1()


