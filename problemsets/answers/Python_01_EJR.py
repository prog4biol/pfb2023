#!/usr/bin/env python3
# ejr: 2023-10-10
# pfb 2023: problem set python 2

### IMPORTS
import sys

### MAIN


# static
activity = "Reading"
animal = "Platypus"


print("Static output:")
print("My name: Eric")
print("My favorite color: Gray")
print("My favorite activity: ", activity)
print("My favorite activity: ", animal)


# command line 
print("\n\n")
print("From Command Line:")

name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

print("My name: " + name)
print("My favorite color: " + color)
print("My favorite activity: " + activity)
print("My favorite activity: " + animal)
