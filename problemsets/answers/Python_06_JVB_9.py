#!/usr/bin/env python3

# 9. Write your first FASTA parser script. This is a script that reads in a FASTA file and stores each FASTA record separately for easy access for future analysis.
#
# Things to keep in mind:
#    - open your file
#    - read each line
#    - is your line a header line? is it a sequence line?
#    - does a single FASTA record have one line of sequence or multiple lines of sequence?
#
#    HINTS: use file I/O, if statements and dictionaries to write your first FASTA parser. Some other useful functions and methods are find, split, string concatenation.
#
#    At the end, your script should return the following:
#
#    fastaDict = {
#       'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' ,
#       'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' ,
#       'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' ,
#       'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }

import sys

fasta_file = sys.argv[1]

fastaDict = {}
sequence_name = None
# We define sequence_name above the loop so that our script can "remember"
# which sequence we are parsing when we get to a sequence line, which occurs
# on separate lines after the sequence_name.
with open(fasta_file, "r") as fasta_input:
    for line in fasta_input:
        line = line.strip()
        if line.startswith(">"):
            # 1) We have a FASTA sequence definition line, the first thing to
            # do is to remove the ">" symbol at the very start of the file.

            # 2) Incase there is space between ">" and the name, we call .lstrip()

            # 3) Then we split the string on the first whitespace (the non-
            # white-space string before the first space is considered the
            # sequence name, everything after is the sequence description.
            # str.split() has an optional keyword argument that you can use
            # to specify how many times to split the string when multiple
            # instances of the split string occurs in the string being split
            defline = line[1:].lstrip().split(maxsplit=1)
            sequence_name = defline[0]
            sequence_name = sequence_name.strip()  
            # we havent seen any sequence for this sequence record yet, so
            # initialized an empty string in our dict to append to:
            fastaDict[sequence_name] = ""
        else:
            # sequence line, append to dict value
            fastaDict[sequence_name] += line

print(fastaDict)
