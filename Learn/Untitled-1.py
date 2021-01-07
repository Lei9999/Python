# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRC-C (^C).")
print("If you do want that, hit RETURE")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Googbye!")
target.truncate()

print(f"The above has been written to the file '{filename}'")