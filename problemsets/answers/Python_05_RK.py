#!/usr/bin/env python3
##Dictionaries problem set

import sys

#Write a dictionary of your favorite things
#Make lists for favorites
book_list=['Charlie and the Chocolate Factory', 'The Name of the Wind', 'Legends and Lattes']
song_list=['Wicked Game','E.T.','Give Me One Reason']
tree_list=['sycamore','pine','paw paw']

#Make a dictionary of favorites with the list of favorites
faves_dict={'book':book_list, 'song':song_list, 'tree':tree_list}
print(f'My favorite things are: {faves_dict}')

#print just favorite book
#note: inner quotes need to be different from f-string quotes
#such as f'normal string here {variable["string key"]}'
#and not f'string {variable['key']}'
print(f'\nMy favorite book is: {faves_dict["book"][1]}')

#print favorite book, but first make the key a variable
book_key='book'
print(f'\nAnother way to call on my absolute favorite: {faves_dict[book_key][1]}')

#print favorite tree
print(f'\nBest tree is {faves_dict["tree"][0]}\n')

#add organism to dictionary
#organism list
org_list=['fish','bugs','squirrels']
faves_dict['critters']=org_list
print(f'The whole dict of favorites looks like: {faves_dict}\n')
print(f'But my new favorites are: {faves_dict["critters"]}\n')

# for loop to print out each key value pair
for each_key in faves_dict: #for each key in dict, do this:
    value=faves_dict[each_key] #the value for each key is:
    print(f'Key: {each_key}, Value: {value}')

#Let the command line input act as a key
#must be an existing key (book, song, tree, critters, user favorite)
#for user favorite key on the command line use "user favorite" with quotes
fetch_key=sys.argv[1]
print(f'The value for {fetch_key} is {faves_dict[fetch_key]} ')

###
#Print out all the keys before taking user input
key_list=[key for key in faves_dict] #list comprehension yo 
print(f'The list of keys is {key_list}') # check that the you made a good list of keys

#Provide the prompt
provide_keys=f'\nPlease from these categories: {key_list}'
print(provide_keys)
user_choice=input('Enter your selection: ')
print(f'The favorites in {user_choice} are {faves_dict[user_choice]}')
###

#change the value of your favorite organism
new_fave_org=['lizards','birds','frogs']
faves_dict['critters']=new_fave_org
print(f'Now my favorite organisms are: {faves_dict["critters"]}')

#Take in a user value for an existing key
user_value=input('Give me a new favorite tree: ')
print(tree_list)
tree_list.append(user_value)
print(tree_list)
faves_dict['tree']=tree_list
print(f'At your suggestion, {user_value} is now one of my favorite trees')
print(f'All of my favorite trees are: {faves_dict["tree"]}')