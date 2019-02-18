#!/usr/bin/python3

# Get the character given by an ASCII number
# char = chr(number)

import sys
import re

if len(sys.argv) == 1:
	print("No arguments passed. Feed me a set of ASCII numbers.")
	print("Example: ./ascii2char.py '100 102 104 98'")
	print("OR")
	print("./ascii2char.py 4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465")
	exit()

else:
	temp = ""
	passed = sys.argv[1]
	# check for letters
	if re.search('[a-zA-Z]', passed):
		# do hex conversion
		asciiHexArray = re.findall('..?', passed)
		for i in asciiHexArray:
			char = bytes.fromhex(i).decode('ascii')
			temp += char
		print("Original ASCII in hex: ",passed,"\nIn char: ",temp)
	else:
		# setup array for splitting the ascii numbers up.
		asciiArray = passed.split()
		for i in asciiArray:
			char = chr(int(i))
			temp += char
		print("Original ASCII numbers: ",passed,"\nIn char: ",temp)
