
## Python Problemset 3: Interactive interpreter portion ##

1. What are considered sequences in Python?
   - A 'sequence' in Python is a data structure that contains an ordered collection of one or (typically) more items, such as `list`s, `tuple`s, and `str`ings.

2. What is the length of the following DNA string? Is this DNA string a Python sequence?
   ```python
   dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

   print("DNA string length:",len(dna))

   # yes, *every* string in Python is a sequence.
   ```

3. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now. It is probably smart to commit after each problem set question.
   ```bash
   git add yourfile.py
   git commit -m 'Initial commit of yourfile.py'
   ```

4. In the interpreter:
	- Create a variable named 'DNA' which contains the sequence above.
	- Count the number of A's  
	- Count the number of T's  
	- Count the number of G's
	- Count the number of C's
	
    ```python
    Python 3.6.15 | packaged by conda-forge | (default, Dec  3 2021, 18:49:43) 
    Type "copyright", "credits" or "license" for more information.

    IPython 5.8.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: dna="GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGC
       ...: GTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACT
       ...: TCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCG
       ...: TGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAA
       ...: GTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAG
       ...: CACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

    In [2]: num_A = dna.count('A')  # use the str.count() method to count the occurances of 'A'

    In [3]: num_T = dna.count('T')  # use the str.count() method to count the occurances of 'T'

    In [4]: num_G = dna.count('G')  # use the str.count() method to count the occurances of 'G'

    In [5]: num_C = dna.count('C')  # use the str.count() method to count the occurances of 'C'

    In [6]: print(f"A: {num_A:d}, T: {num_T:d}, G: {num_G:d}, C: {num_C:d}")
    A: 167, T: 187, G: 218, C: 270

    ```

5. In the interpreter:
	- Create a variable named 'bird' with the contents 'chicken'
	- convert the contents of 'bird' to be uppercase and print

    ```python
    Python 3.6.15 | packaged by conda-forge | (default, Dec  3 2021, 18:49:43) 
    Type "copyright", "credits" or "license" for more information.

    IPython 5.8.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: bird = "chicken"

    In [2]: print(bird.upper())  # use the string.upper() method to uppercase all str chars
    CHICKEN

    ```


