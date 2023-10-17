#!/usr/bin/env python3

# Write a script that uses a while loop to print out the numbers 1 to 100.

tracker = 1
while tracker < 101:
    print(tracker)
    tracker += 1



# Write a script that uses a while loop to calculate the factorial of 1000.

tracker   = 1
factorial = 1 
while tracker < 1001:
    factorial = factorial * tracker
    tracker += 1

print(factorial)

print("\n")

## the following uses the "math" package to do the same thing
import math
 
print(math.factorial(1000))


# Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]

my_numbers = [101,2,15,22,95,33,2,27,72,15,52]

for i in my_numbers:
    print(i)


print("\n Print out only the values that are even (hint: use the modulus operator).")

# Print out only the values that are even (hint: use the modulus operator).

for i in my_numbers:
    if not i%2:
        print(i)


print("\n # Sort the elements of the above list, then iterate through each element using a for loop and print each")
# Sort the elements of the above list, then iterate through each element using a for loop and:
# Print each element.

my_sorted_list = sorted(my_numbers)

for i in my_sorted_list:
    print(i)


print("# Calculate two cumulative sums, one of all the even values and one of all the odd values.")

odds  = 0
evens = 0

for i in my_sorted_list:
    if not i%2:
        odds += i
    else:
        evens += i


# Print only the final two sums. The output from your script should be:
# Sum of even numbers: 150 
# Sum of odds: 286

print("Odds cumsum:", odds, "Evens cumsum:", evens)



# Write a script that uses range() in a for loop to print out every number between 0 and 99

# Modify your loop to print out every number between 1 and 100.
# Create a new script that uses list comprehension to do the same thing as problem 8. (Use range() to print out every number between 1 and 100.)

# Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

# Modify your script so that it will only print the number if it is odd.
# Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and:

# Print out each element.
# Print out the length and the sequence, separated by a tab. The output should look like:
# 14	ATGCCCGGCCCGGC
# 25	GCGTGCTAGCAATACGATAAACCGG
# 12	ATATATATCGAT
# 8	ATGGGCCC
# Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].

# Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")

# Have you been commiting you work?
