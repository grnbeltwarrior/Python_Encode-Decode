#!/usr/bin/python3
# Example: bin2hex.py 0001101010

import sys

if len(sys.argv) == 1:
  print("No arguments passed. Feed me a binary.")
  exit()
else:
  binary = sys.argv[1]
  temp = int(binary,2)
  print("Original in binary: ",binary,"\nIn hexadecimal: ",hex(temp))
