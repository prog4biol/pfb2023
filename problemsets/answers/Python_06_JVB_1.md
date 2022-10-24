
1. Make a set using the two different syntaxes for creating a set `myset = set()` and `myset2 = {}`. What is the difference? Does it matter how you make it?
```
mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}
```

    - Answer: Yes, it does matter. Calling the `set()` class constructor inputs any sequence (sensu Python) object and iterates over that sequence to create a new set object instance with each distinct item (here, nucleotides) represented once. If we wanted to create a set with `ATGTGGG` as a single string, we would need to pass it in as a list/tuple of strings (i.e.: `set(('ATGTGGG',))`) or using `{...}`. Calling `{...}` inputs sequences as-is.

