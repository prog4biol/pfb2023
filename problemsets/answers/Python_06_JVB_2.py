#!/usr/bin/env python3
# JVB 2023-1017

# 2. Write a script to find the intersection, difference, union, and symetrical difference between these two sets.
#
# ```
# Set A = 3 14 15 9 26 5 35 9
# Set B = 60 22 14 0 9
# ```

setA = set((3, 14, 15, 9, 26, 5, 35, 9))
setB = set((60, 22, 14, 0, 9))

print("Intersection:")
print(setA.intersection(setB))  # or, equivalently: print(setA & setB)

print("Difference (A - B):")
print(setA.difference(setB))  # or, equivalently: print(setA - setB)

print("Difference (B - A):")
print(setB.difference(setA))  # or, equivalently: print(setB - setA)

print("Union (inclusive 'OR'):")
print(setA.union(setB))  # or, equivalently: print(setA | setB)

print("Symmetric difference (exclusive 'OR'):")
print(setA.symmetric_difference(setB))  # or, equivalently: print(setA ^ setB)

