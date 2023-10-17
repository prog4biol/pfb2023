Python 2 Problem Set -- Operators, Truth, Logic
===================

1. Use the Interactive Interpretor to test to see if you can find an ['ATG' in](https://github.com/prog4biol/pfb2023#membership-operators) the following DNA string:

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

2. How about 'TTT'?

3. If you didn't already save the DNA string to a variable, do that now and redo [1 and 2](https://github.com/prog4biol/pfb2023#membership-operators).

```
>>> dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> 'ATG' in dna
False
>>> 'TTT' in dna
True

```


4. In the interpretor use `bool` to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.


```
>>> bool('')
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(FALSE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FALSE' is not defined
>>> bool(false)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> bool(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> bool(True)
True
>>> bool('True')
True
>>> bool('False')
True


```


Part 2.1: Python_02_KLG_1.py
Part 2.2-2.10: Python_02_KLG_2.py
