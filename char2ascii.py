#!/usr/bin/python3

# Get the ASCII number of a character
# number = ord(char)

import sys

if len(sys.argv) == 1:
	print("No arguments passed. Feed me a string.")
	exit()

else:
	temp = ""
	passed = sys.argv[1]
	for i in passed:
		number = ord(i)
		temp += "x\\" + str(number)
	print("Original string: ",passed,"\nIn ASCII number: ",temp)
