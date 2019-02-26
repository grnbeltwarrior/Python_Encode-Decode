#!/usr/bin/python3

import sys
import codecs

def hex2text(hex):
  temp = ''.join(hex.split())
  result = codecs.decode(temp,'hex').decode('utf-8',errors='ignore')
  return result

if len(sys.argv) == 1:
  print("No arguments passed. Feed me a hex string.")
  exit()
else:
        hex = sys.argv[1]
        print("Original hex: ",hex,"\nConverted to text: ",hex2text(hex))
