#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 6
# find apoI restriction siee and prince occurances

# FASTA format:
#>header
#ATGCATGCATGC

# print all FASTA headers in a file
import re
site="[AG]^AATT[CT]"


# read fasta file into dictionary
header = ""
fasta_dict = {}
with open("Python_07_ApoI.fasta","r") as f_obj: 
	# iterate over each line in file
	for line in f_obj:
		line = line.rstrip() # remove newline

		# match only looks at the first character which makes it fast
		if re.match(">", line):
			header = line
			fasta_dict[header] = ''
		else:
			fasta_dict[header] += line

for header in fasta_dict:
   fasta_dict[header] = re.sub(r"([AG])(AATT[CT])" , r"\1^\2" , fasta_dict[header])



# print out FASTA dictionary
for header in fasta_dict:
  print(header)
  # add newlines every 60 characters
  seq = re.sub("(.{60})", "\\1\n", fasta_dict[header])
  print(seq)
