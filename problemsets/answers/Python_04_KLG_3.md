
# Problem 3

Using the Python interpreter, interrogate the difference between these two ways to copy a list. Careful! One of these is NOT what you might expect.

## Method 1

Create a list. For example: my_list = ['a', 'bb', 'ccc']

Make a copy using the = assignment operator: list_copy = my_list

Print the original list print(my_list)

Alter the list_copy by adding a new element using append()

Print the original list again print(my_list)

```
>>> my_list = ['unicorns', 'mermaids', 'witches']
>>> my_copy = my_list
>>> print(my_list)
['unicorns', 'mermaids', 'witches']
>>> my_copy.append('pixies')

>>> print(my_list)
['unicorns', 'mermaids', 'witches', 'pixies']
>>> print(my_copy)
['unicorns', 'mermaids', 'witches', 'pixies']
```




## Method 2

Create a list. For example: my_list2 = ['a', 'bb', 'ccc']

Make a copy with the copy() method list_copy2 = my_list2.copy()

Print the original list print(my_list2)

Alter the list_copy2 by adding a new element using append()

Print the original list again print(my_list2)


```
>>> my_list = ['unicorns', 'mermaids', 'witches']
>>> my_copy = my_list.copy()
>>> my_list
['unicorns', 'mermaids', 'witches']
>>> my_copy.append('pixies')
>>> my_list
['unicorns', 'mermaids', 'witches']
>>> my_copy
['unicorns', 'mermaids', 'witches', 'pixies']

```


The difference is that the copy method makes and unlinked copy of the original list, whereas the assignment operator tracks the original version.