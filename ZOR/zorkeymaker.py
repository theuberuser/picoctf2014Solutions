#!/usr/bin/python

import sys

"""
Daedalus Corporation encryption script.
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        key ^= ((2 * ord(ch) + 3) & 0xff)
#    print "KEY: %d" % key
    return xor(input_data, key)

def decrypt(input_data, password):
    return encrypt(input_data, password)


def main():
    #string = "HELLO WORLD"
    result_data = ""
    #resulted_data = encrypt(string, sys.argv[1])
    #ciphertext = resulted_data
    #print "ENCRYPTED DATA: " + ciphertext
    resulted_data = decrypt(sys.argv[1], sys.argv[2])
    plaintext = resulted_data
# UNCOMMENT LINES FOR TESTING    
#if plaintext == "THE PASSWORD IS NOT PASSWORD":
    #  print "YOU CRACKED THE CODE!!!!"
    #else:
    #  print "KEY INVALID"

    print plaintext
main()
