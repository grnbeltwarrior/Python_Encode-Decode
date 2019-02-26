#!/usr/bin/python3

import sys

def to_hex(str):
        return int(str,base=16)

def xor_2strings(strA, StrB):
        a = to_hex(strA)
        b = to_hex(strB)
        return hex(a ^ b)

if len(sys.argv) == 1:
        print("No arguments passed. Feed me some strings (2).")
        print("Example: ./xor_strings.py 1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965")
        exit()

else:
        strA = sys.argv[1]
        strB = sys.argv[2]
        print(xor_2strings(strA,strB))
