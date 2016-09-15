import sys
import os
import random


# Functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


string = addNumber(1, 4)  # Function Calling
print(string)

print("What is your name ?")
name = sys.stdin.readline()  ## User Defined Input
print("Hello", name)

long_str = "I'll catch you if u fall - The Floor"

print(long_str[0:4])  # Print from 0 to 4th index of string

print(long_str[-5:])  # Print last 5 letters of the sentence

print(long_str[:-5])  # Print from start of string till 5th letter from back (5th letter from back not included)

print(long_str[:4] + " be there")  # leaving blank index is same as 0 here --> this is an example of string concat

# formatted string format -> print("%c %d" %('A',23)) ; here arguments in bracket are the values for %c and %d
print("%c is my %s letter and my number %d is %.5f" %  # %.5f means upto 5 decimal places
      ('X', "favourite", 5, 0.14))

print(long_str.capitalize())  # It capitalize 1st ltter of the string

print(long_str.find("Floor"))  # It finds the index of first occurence of this substring

print(
    long_str.isalnum())  # Check if all string are letters or numbers, if there is even a single number, it'll return true else it'll return false

print(len(long_str))  # String Length

print(long_str.replace("Floor",
                       "Ground"))  # Replace the value of the given substring with other (temporary here only inside print function)

print(long_str.strip())  # Remove white spaces from string

quote_list = long_str.split(" ")  # Split the String and store them into a list  when blank space occurs

print(quote_list)
