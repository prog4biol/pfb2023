#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 4

# FASTA format:
#>header
#ATGCATGCATGC

# print all FASTA headers in a file
import re

# open file
with open("Python_07.fasta","r") as f_obj: 
  # iterate over each line in file
  for line in f_obj:
    line = line.rstrip() # remove newline

    # match only looks at the first character which makes it fast
    if re.match(">", line):

      # using finditer and groups
      for matches in re.finditer(r">(.+?) (.+)", line):
        print("id:", matches.group(1), "desc:", matches.group(2))

      # using regex substitution
      print(re.sub(r">(.+?) (.*)" , r"id: \1 desc: \2" , line))
