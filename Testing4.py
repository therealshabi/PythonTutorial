import random
import os
import sys

# File I/O / File Handling

test_file = open("test.txt", "wb")  ##Opens the file if creaated/not created in write mode

print(test_file.mode)  ##Print the mode of file opened

print(test_file.name)  ##Print the name of the file opened

test_file.write(bytes("Write me to the file\n", 'UTF-8'))  ##writing into the file

test_file.close()  # Closing the file

test_file = open("test.txt", 'r+')  # Reopening an existing file in Read Mode

text = test_file.read()  # Reading the text from the file

print(text)

os.remove("test.txt")  # Removing the file/Deleting the file
