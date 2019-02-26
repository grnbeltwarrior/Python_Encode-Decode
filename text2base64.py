#!/usr/bin/python3

import base64
import sys

if len(sys.argv) == 1:
        print("No arguments passed. Feed me some text.")
        print("Example: ./text2base64.py 'I'm a little teapot.'")
        print("OR")
        print("./text2base64.py 'I'm a little teapot.'")
        exit()

else:
        temp = ""
        passed = sys.argv[1]
        temp = base64.b64encode(bytes(passed, 'utf-8'))
        temp = temp.decode('utf-8')
        print("Original text: ",passed,"\nIn Base64: ",temp)
