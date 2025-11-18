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


# def likelihood():
#     likelihoods = (50, 38, 27, 99, 4)
#     return likelihoods
#
#
# def run_task1():
#     hood = likelihood()
#     print(f"Minimum likelihood of falling: {min(hood)}% ")
#
#
# if __name__ == "__main__":
#     run_task1()


###############################################################
# Activity 2 Tuple Return Type


# def likelihood_min_max():
#     likelihoods = (50, 38, 27, 99, 4)
#     min_value = f"Minimum likelihood of falling: {min(likelihoods)}%"
#     max_value = f"Maximum likelihood of falling: {max(likelihoods)}%"
#     print(min_value)
#     print(max_value)
#
#
# def run_task2():
#
#     likelihood_min_max()
#
#
# if __name__ == "__main__":
#     run_task2()


###################################################################
# Activity 3: Nested Tuples


# def steps():
#     likelihoods = [
#         ("step 1", 50),
#         ("step2", 38),
#         ("step3", 27),
#         ("step4", 99),
#         ("step5", 4),
#     ]
#     return likelihoods
#
#
# def run_task3():
#     new_steps = steps()
#     good_steps = []
#     bad_steps = []
#
#     for step in new_steps:
#         if step[1] >= 50:
#             bad_steps.append(step)
#         else:
#             good_steps.append(step)
#
#     print(f"Good steps {len(good_steps)}, Bad steps {len(bad_steps)}")
#
#
# if __name__ == "__main__":
#     run_task3()


# import array as arr
#
# number = arr.array("i", [1, 2, 3, 4, 5])
#
# for i in number:
#     print(i * 3)


# Create a student marks .
# Convert them into tuple
# Sort the list
# Create an array from the sorted list
# Multiply all array elements by 2


import array as arr


marks = [78, 92, 65, 88, 70]
marks_tuple = tuple(marks)
sorted_marks = sorted(marks)
marks_array = arr.array("i", sorted_marks)
result = arr.array("i", (x * 2 for x in marks_array))

print(result)
