FASTA tool
==========

Create a python script that can be called on the command line that takes arguments to indicate the action to be performed on a given nucleotide FASTA file.

Example Functionality:

1. FASTA stats: provide a FASTA file and return some common FASTA stats
```
./fasta_multi_tool.py stats myfasta.fa
myfasta.fa
Seq Count: 10
Max len: 2000
Min len: 100
Avg len: 650
N50: 1000
L50: 5
GC%: 55%
```

2. Reverse complement: provide a FASTA file and return FASTA formated output containing the reverse complement of all sequences contained in the input FASTA.
```
./fasta_multi_tool.py revcomp myfasta.fa
```

3. Subseq: provide a FASTA file, a seq ID, and a coordinate range. Return a FASTA formated sequence containing the subseq requested
```
./fasta_multi_tool.py subseq myfasta.fa seqName 5:100
```

4. Translation: provide FASTA file of nucleotide sequences and return FASTA formated tranlslated protein sequence
```
./fasta_multi_tool.py translate myfasta.fa
```

5. Split:  provide FASTA file. Return the number of files requested with the sequences in the input FASTA split across that file count
```
./fasta_multi_tool.py split myfasta.fa 10  

```

6. Specific restriction cutter: Provide FASTA and a restriction enzyme name. Return the count of fragments produced in each sequences and the sequence and length of each fragment in each provided sequence.
```
./fasta_multi_tool.py thiscutter myfasta.fa EcoR1  

```  

7. Restriction cutter finder. Which enzymes cut my seq?: Provide a FASTA file and return a list of each enzyme that will cut each sequecnes and the number of fragments in each sequence for each cutter and the average length of fragments produced for each sequence.
```
./fasta_multi_tool.py findcutter myfasta.fa
```  

8. Pattern search: Provide a FASTA and a pattern, search each sequence in input FASTA for a pattern. Return a bed file with all the matching sequences names and coordinates of match. 
```  
./fasta_multi_tool.py search myfasta.fa TATTAT 
./fasta_multi_tool.py search myfasta.fa '[G|A].CTC' 
```   

9. Wrapper. Reformat fasta to sequences lines of provided length. Provide FASTA file and return FASTA formated sequence of provided length
```
./fasta_multi_tool.py wrap myfasta.fa 60 
```  

10. Masking. Uppercase every nucleotide then lower case all sequence matching provided pattern. Return FASTA formated sequence
```
./fasta_multi_tool.py mask myfasta.fa TATATA 
```  

11. Uppercase all sequences.
```
./fasta_multi_tool.py upper myfasta.fa 
```  

12. Lowercase all sequences.
```
./fasta_multi_tool.py lower myfasta.fa 
```  

13. Longest ORF: Provide a FASTA file, calculate the 6 reading frames, find the longest open reading frame. Return FASTA formated nucleotide sequence with the reading frame of the longest orf reported as well as the length of the longest ORF reported in the header.  
```
./fasta_multi_tool.py orf myfasta.fa 
```  

14. Translated longest ORF: Provide a FASTA file, calculate the 6 reading frames, find the longest open reading frame. Return the translated protein in FASTA formated with the reading frame and length of protein reported in the FASTA header.  
```
./fasta_multi_tool.py orf myfasta.fa 
```

15. Shuffled sequence: Provide a FASTA file, shuffle each sequence. Return a FASTA formated shuffled sequence for each sequence in the provided FASTA file. 
```
./fasta_multi_tool.py shuffle myfasta.fa 
```

16. Any other functionality you would like to see? Add it.

17. Make it so that your script takes a file or FASTA from standard-in so that you can pipe from one tool into another
```
./fasta_multi_tool.py lower myfasta.fa  | ./fasta_multi_tool.py wrap 60
```  

18. Make a module that contains classes with attributes methods.
19. Use exceptions to inform users when they give the wrong input.
20. If you have time, create a protein FASTA multi tool as well. 
