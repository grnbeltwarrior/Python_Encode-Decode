
#!/usr/bin/python3

import sys
import codecs

if len(sys.argv) == 1:
  print("No arguments passed. Feed me a hex string.")
  exit()
else:
        hex = sys.argv[1]
        temp = ''.join(hex.split())
        result = codecs.decode(temp,'hex').decode('utf-8',errors='ignore')
        print("Original hex: ",hex,"\nConverted to text: ",result)
