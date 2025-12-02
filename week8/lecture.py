fruits = {"apple", "banana", "cherry"}
empty_set = set()

# key properties
s = {1, 2, 3, 3, 4, 4, 5}

print(s)

# Common set operations

s = {1, 2, 3}
s.add(4)
s.remove(2)  # error if missing
s.discard(10)  # no error if missing

print(s)


print(3 in s)
print(5 not in s)

# Union intersection and difference

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# Dictionaries
person = {"name": "Alice", "age": 25}
empty_dict = {}

# Access and Modify

print(person["name"])
person["city"] = "London"
print(person)
person["age"] = 25
print(person)


print(len(person))
print("age" in person)
print(person.pop("age", None))
person.pop("age", None)
print(person)
print(person.popitem())
print(person)
print(person.values())
person.clear()
print(person)


# Task
# Write a program that tracks how many unique people visited a shop today.
#
# Task Requirements:
#
# Create an empty set called visitors.
#
# Ask the user to enter 5 names.
#
# Add each entered name to the set.

visitors = set()

for _ in range(5):
    visitors.add(input("Enter visitor name: "))

print(visitors)
