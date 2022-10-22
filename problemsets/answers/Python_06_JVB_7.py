#!/usr/bin/env python3


# 7. Open and print the reverse complement of each sequence in
#   [Python_06.seq.txt](https://raw.githubusercontent.com/prog4biol/pfb2022/master/files/Python_06.seq.txt).
#   Each line is the following format:    `seqName\tsequence\n.`
#   Make sure to print the output in fasta format including the sequence name and a note in the description
#   that this is the reverse complement. Print to STDOUT and capture the output into a file with a command
#   line redirect '>'. 
#    - **Remember is is always a good idea to start with a test set for which you know the correct output.**

with open("Python_06.seq.txt", "r") as file_input:
    for line in file_input:
        line = line.rstrip()       # remove the \n
        fields = line.split("\t")  # split only on \t

        sequence_name = fields[0]
        forward_sequence = fields[1].lower()  # normalize all nucleotides to lowercase

        reverse_sequence = forward_sequence[::-1]  # reverse the sequence
        revcomp_sequence = reverse_sequence.replace('a','T')  # convert A => T
        revcomp_sequence = revcomp_sequence.replace('t','A')  # convert T => A
        revcomp_sequence = revcomp_sequence.replace('c','G')  # convert C => G
        revcomp_sequence = revcomp_sequence.replace('g','C')  # convert G => C

        print(f">{sequence_name}\n{revcomp_sequence}")

