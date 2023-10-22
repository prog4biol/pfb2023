#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 6
# find apoI restriction siee and print occurances

import re


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
  seq_list = re.split("\^", fasta_dict[header])
  seq_list.sort(key=len, reverse=True)

  print("\t".join(seq_list))
