import random
import sys
import os

print("Shahbaz\'s friend is so cool\n")
multi = '''I am very
cool'''  # Multiline String
# print(multi,end="")


#### Lists

groc_list = ["Banana", "Apple"]
groc_list[1] = "Grapes"
print(groc_list[0:2])  # here index 2 is not included
other_things = ["Washing Car", "Driving", "Shopping"]
to_do_list = [other_things, groc_list]  # List of Lists
print(to_do_list[0][2])  # here you chose the first list in the to_do_list and 2nd item on that list
groc_list.append("Apples")
print(to_do_list)
groc_list.insert(1, "Apples")  # Insert to specific Index
print(to_do_list)
groc_list.sort()  # Sorting the list
print(groc_list)
print("\n", to_do_list)

groc_list.remove("Apples")
print(groc_list)

del groc_list[0]  # Deleting at specific index
print(groc_list)

print(max(other_things))  # returns max String
print(len(to_do_list))

to_do_list2 = other_things + groc_list  # Combining Lists like Strings
print(to_do_list2)

# Tuples  -- They can't be changed after it's created unlike Lists---for data which we don't wnt be changed
# remember it starts with small braces

pi_tuple = (1, 2, "Shahbaz")
print("\n", pi_tuple)
new_list_pi_tuple = list(
    pi_tuple)  # Conversion of Tuple to List and we can also do vice versa by function tuple(<list>)
print("\n", new_list_pi_tuple)
# functions like len(), min(), max() can also be used by a tuple

# Dictionary/Maps - Key Value Pairs (can't use + operator for joining Maps

super_villains = {"Name": "Shahbaz", "Batch": "B2"}
print("\n", super_villains["Name"])
del super_villains["Batch"]
print(super_villains)
super_villains["Name"] = "Aaliya"
print(super_villains.get("Name"))
super_villains['Batch'] = "B2"  # Inserting Values in Dictionary
print(super_villains.keys())  # Display all keys
print(super_villains.values())  # Display all values
