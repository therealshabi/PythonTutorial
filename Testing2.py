import os
import sys
import random

age = 16
name = "SRK"

##IF CONDITIONS

if age > 16:  # remember ':' and indentation
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")

if age >= 21:
    print("You are old enough to drive")
elif age >= 16:  ##Same as else if
    print("You are old enough to drive a bike")
else:
    print("You are not old enough to drive")

if (age >= 1 and age <= 18 and name != "Shahbaz" and name != "SRK"):  # Here '&&' or '||' does not work
    print("You are not old enough to drive anything")
elif (age > 18 or name == "Shahbaz"):
    print("The Name is Shahbaz")
elif not (name == "Shahbaz"):  # This works as a not(!) operator
    print("Only Shahbaz is eligible for Driving")

##LOOPS

for i in range(0, 10):
    print(i, end=" ")  # end=" " --> to print on same line
print()  # Single line change
grocery_list = ["Bananas", "Apples", "Grapes"]
for i in grocery_list:
    print(i)

num_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
print()
for i in num_list:
    print(i)

for i in range(0, 4):  ##Number of rows in 2D List is 4
    for j in range(0, 3):  ##Number of coloumns in 2D List is 3
        print(num_list[i][j])

# For generating random number we should import random
random_num = random.randrange(0, 16)  # Random Number function called for range (0,100), where 100 is not included
print()
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 16)  # Generating new random number

i = 0

## We can use break and continue statement even here

while i <= 20:
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
    i += 1
