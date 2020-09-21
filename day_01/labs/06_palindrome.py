# A program to jumble the word
# Input: apples
# Output: elpaps

import random

# input the string

s = input("Enter a string: ")

# split the characters

chars = list(s)

# randomize the order of charaters

random.shuffle(chars)

# rejoin the characters

outchar = ''.join(chars)

# present the output

print("Jumbled version: ", outchar)
