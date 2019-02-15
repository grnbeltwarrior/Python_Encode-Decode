#!/usr/bin/python3

import sys
import base64

if len(sys.argv) == 1:
	print("No arguments passed. Feed me a base64 string.")
	exit()
else:
	base = sys.argv[1]
	result = (base64.b64decode(base)).decode('utf-8')
	print("Original Base64: ",base,"\nConverted to text: ",result)
