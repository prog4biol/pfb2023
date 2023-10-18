#!/usr/bin/env python3

### Problem 2
# Write a script that splits a string into a list. In your script:

# Save the string sapiens, erectus, neanderthalensis as a variable named taxa.

taxa = 'sapiens, erectus, neanderthalensis'

# Print taxa.

print(taxa)

# Print taxa[1], what do you get?

print(taxa[1]) ## returns "a"



# Print type(taxa). What is it's type?


print(type(taxa))
## <class 'str'>


# Split taxa into individual words and print the result of the split. (Think about the ', '.)

print(taxa.split(', '))


# Store the result of split in a new variable named species.

species = taxa.split(', ')

# Print species.

print(species)

# Print the species[1], What do you get?

print(species[1])
## returns 'erectus'


# Print type(species). What is it's type?

print(type(species))

## returns <class 'list'>


# Sort the list alphabetically and print (hint: lookup the function sorted()).

print(sorted(species))
## returns ['erectus', 'neanderthalensis', 'sapiens']


# Sort the list by length of each string and print. (The shortest string should be first). Check out documentation of the key argument.

print(sorted(species, key=len))

## returns ['sapiens', 'erectus', 'neanderthalensis']
