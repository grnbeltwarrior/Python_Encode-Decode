#!/usr/bin/python3

import sys
from urllib.parse import unquote

if len(sys.argv) == 1:
	print("No arguments passed. Feed me a set of ASCII numbers.")
	print("Example: ./ascii2char.py '100 102 104 98'")
	exit()

else:
	passed = sys.argv[1]
	url = unquote(passed)
	print("Original: ",passed,"\nURL decoded: ",url)
