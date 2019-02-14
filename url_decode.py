#!/usr/bin/python3

import sys
from urllib.parse import unquote

if len(sys.argv) == 1:
	print("No arguments passed. Feed me a URL encoded string.")
	print("Example: ./url_decode.py %63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64")
	exit()

else:
	passed = sys.argv[1]
	url = unquote(passed)
	print("Original: ",passed,"\nURL decoded: ",url)
