
```python
Python 3.6.15 | packaged by conda-forge | (default, Dec  3 2021, 18:49:43) 
Type "copyright", "credits" or "license" for more information.

IPython 5.8.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: # Problem 1: Is string 'ATG' a substring of the larger sequence below?

In [2]: 'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
Out[2]: False

In [3]: # Problem 2: Is string 'TTT' a substring of the larger sequence below?

In [4]: 'TTT' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
Out[4]: True

In [5]: # Problem 3: Assign the large string to a variable (saves key strokes)

In [6]: dna = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"

In [7]: 'ATG' in dna
Out[7]: False

In [8]: 'TTT' in dna
Out[8]: True

In [9]: # Problem 4: In the interpretor use bool to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.

In [10]: bool('')  # an empty string (no characters)
Out[10]: False

In [11]: bool(0)  # an integer 0 is always False
Out[11]: False

In [12]: bool(0.0)  # a float 0 is also always False
Out[12]: False

In [13]: bool(FALSE)  # This is not a recognized Python keyword, so unless 'FALSE' is quoted, an exception will be raised
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-9cd20817227a> in <module>()
----> 1 bool(FALSE)

NameError: name 'FALSE' is not defined

In [14]: bool("FALSE")  # Same as above, but now quoted. "FALSE" is a non-zero lengthed string, so will always test True.
Out[14]: True

In [15]: bool("false")  # "false" is also a non-zero lengthed string, so will always test True.
Out[15]: True

In [16]: bool("True")  # "True" is a non-zero lengthed string, so will always test True.
Out[16]: True

In [17]: bool(True)  # True is always True
Out[17]: True

In [18]: bool("true")  # "true" is a non-zero lengthed string, so will always test True.
Out[18]: True

In [19]: bool("False")  # "False" is a non-zero lengthed string, so will always test True.
Out[19]: True

In [20]: bool(False)  # False is always False
Out[20]: False

```
