#!/usr/bin/env python3
"""
Zachary Konkel
2023/10/11 
Python 5 - Dictionaries and Sets - Problem Set
Programming for Biology 2023
"""

# 1. write a script in which you construct a dictionary of your favroite things
favorite_things_dict = {'book': 'wandering on the way', 
                        'song': 'trevor hall - samay', 
                        'tree': 'cedar'}

# 2. print out your favorite book
print(favorite_things_dict['book'])

# 3. print out your favorite book but use a variable in the key
fav_thing = 'book'
print(favorite_things_dict[fav_thing])

# 4. print favorite tree
print(favorite_things_dict['tree'])

# 5. add your favorite organism to the dictionary using "fav_thing" as the
# variable
fav_thing = 'organism'
favorite_things_dict[fav_thing] = 'psilocybe'
print(favorite_things_dict[fav_thing])

# 6. Take a value from the command line for fav_thing and print the value 
# of that item from the dictionary. Maybe you want to print out all the keys
# to the user so that they know what to pick from. Check out input(). 
fav_thing_keys = ', '.join(list(favorite_things_dict.keys())) # this is
# creating a string of the keys within the dictionary

fav_thing = input('Input the favorite thing type you want (' + fav_thing_keys \
                + '):') # I've gone a bit beyond here to inform the user of the
                # keys that are in the dict, thereby preventing unknown KeyErrors
print(favorite_things_dict[fav_thing])

# 7. Change the value of your favorite organism
favorite_things_dict['organism'] = 'athelia'

# 8. Get the fav_thing from the command line and a new value for that key. 
# Change the value with the user inputted value.

new_fav_key = input('Add a new type of favorite thing: ')
new_fav_thing = input('Add your favorite item of that thing: ')
favorite_things_dict[new_fav_key] = new_fav_thing

# 9. Use a for loop to print out each key and value of the dictionary
# I'm going to use the faster way to do this
for key, val in favorite_things_dict.items():
    print(key, val)

# 10. Make a set using the two different syntaxes for creating a set; does it
# matter? What is the difference if so?
my_set = set('ATGCCT')
my_set2 = {'ATGCCT'}
# the difference is that my_set2 is going to make the entire string an entry in
# the set, whereas set() is going to fragment the string into its individual
# chars; we can evaluate this if the strings are the same via:
print(my_set == my_set2)

# 11. Write a script to find the intersection, difference, union, and
# symmetrical difference between these two sets.
set_a = {3, 14, 15, 9, 26, 5, 35, 9}
set_b = {60, 22, 14, 0, 9}
print('Intersection', set_a.intersection(set_b))
print('Difference', set_a.difference(set_b))
print('Union', set_a.union(set_b))
# important to note that the intersection and difference will vary depending on
# the order, e.g. set_a.difference(set_b) != set_b.difference(set_a)

# 12. If you create a set using a DNA sequence, what will you get back?
seq   = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAA' \
      + 'AGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTG' \
      + 'GGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCAC' \
      + 'TGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGA' \
      + 'CCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTT' \
      + 'GATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAG' \
      + 'AATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCA' \
      + 'CCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGT' \
      + 'TTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTC' \
      + 'AACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCG' \
      + 'CCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGG' \
      + 'CGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGA' \
      + 'GTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCC' \
      + 'CATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAG' \
      + 'CAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGA' \
      + 'CACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGA' \
      + 'TCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAA' \
      + 'CAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGA' \
      + 'ACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCC' \
      + 'GTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCA' \
      + 'TCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCT' \
      + 'GGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCC' \
      + 'AAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATG' \
      + 'GCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGC' \
      + 'TCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAG' \
      + 'TATTTGGATGAC'
# well, it depends on the way you specify set! see problem 10.

# 13. Write a script that determines the unique nucleotides in that sequence
# and iterate over each unique character, store in a dict, report the count of
# each character, and report the GC content
uniq_chars = set(seq)
char_dict = {}
for uniq_char in list(uniq_chars): # you don't need to turn it into a list, but
# it is faster to iterate over a list than a set
    char_dict[uniq_char] = seq.count(char)
total_len = len(seq)
for uniq_char, occurrences in char_dict.items():
    print(uniq_char + ': ' + str(occurrences)) # note I'm not using commas in
    # print, so I must specify changing the int occurrences to a string
print('GC: ' + str((char_dict['G'] + char_dict['C'])/total_len) * 100 + '%')

# WOOHOO!
