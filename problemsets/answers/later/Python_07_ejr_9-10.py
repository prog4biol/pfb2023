#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 6
# read in list of cutsites, take an enzyme name and a FASTA file and output 
# 1. the sequence with cut sites
# 2. the number of fragments
# 3. the unsorted fragments
# 4. largest to smallest sorted fragments

import re
import sys

fasta_file = sys.argv[1]
my_enzyme = sys.argv[2]


####
# Read in enzyme file 
####

i=0
enzymes={}
with open("bionet.txt") as enzyme_file:
  for line in enzyme_file:
    line = line.rstrip() # remove newline
    if i < 11:
      i = i + 1
    else:
      fields = re.split("  +", line)
      if len(fields) == 2:
        enzymes[fields[0]] = fields[1]
     
##convert enzymes to patterns
for enzyme in enzymes:
  # add parens
  enzymes[enzyme] = re.sub("(.*)\^(.*)", r"(\1)(\2)", enzymes[enzyme])
  # IUPAC Ambiguity Codes
  enzymes[enzyme] = re.sub("N", r"[ATGC]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("Y", r"[TC]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("R", r"[AG]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("W", r"[AT]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("S", r"[GC]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("B", r"[CGT]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("H", r"[ACT]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("D", r"[AGT]", enzymes[enzyme])
  enzymes[enzyme] = re.sub("V", r"[ACG]", enzymes[enzyme])

#for enzyme in enzymes:
#  print(enzyme, enzymes[enzyme])
#exit()    

####
# read fasta file into dictionary
####
header = ""
fasta_dict = {}
with open(fasta_file,"r") as f_obj: 
	# iterate over each line in file
	for line in f_obj:
		line = line.rstrip() # remove newline

		# match only looks at the first character which makes it fast
		if re.match(">", line):
			header = line[1:]
			fasta_dict[header] = ''
		else:
			fasta_dict[header] += line

####
# OUTPUT
####
# 1. the sequence with cut sites
# 2. the number of fragments
# 3. the unsorted fragments
# 4. largest to smallest sorted fragments
for header in fasta_dict:
   fasta_dict[header] = re.sub(enzymes[my_enzyme] , r"\1^\2" , fasta_dict[header])


# print out FASTA dictionary
for header in fasta_dict:
  print("SeqName:", header)
  print("Sequence:", fasta_dict[header])
  seq_list = re.split("\^", fasta_dict[header])
  print("Unsorted Fragments:", "\t".join(seq_list))
  sorted_seqs = sorted(seq_list, key=len, reverse=True)
  print("Number of Fragments:", len(seq_list))
  print("Sorted Fragments:", "\t".join(sorted_seqs))
