#!/usr/bin/env python3
# regular expression cutter 
# by Sofia Robb

import sys
import re


# enzyme name + cut pattern info
# need to download this file to working directory
# ftp://ftp.neb.com/pub/rebase/bionet.txt 


# get user input
try: 
  fastafile = sys.argv[1]
except:
  print("Missing FASTA file name. Please provide a FASTA file.") 
  exit()


try:
  enzyme = sys.argv[2]
except:
  print("Missing enzyme name. Please provide an enzyme name. ie EcoRI")
  exit()


## parse FASTA file into dictionary
seqs={}
with open(fastafile,"r") as fh:
  id = ''
  for line in fh:
    line = line.rstrip()
    match = re.match(r"^>(\S+)",line)
    if match:
      id=match.group(1)
      seqs[id]=''
    else:
      seqs[id]+=upper(line)

## parse cutter file into dictionary
cutters={}
with open("bionet.txt","r") as fh:
  for line in fh:
    line = line.rstrip()
    match = re.search("(.+)\s+((\w*)\^(\w*))$",line)
    if match:
      cuttername = match.group(1)
      cutleft=match.group(3)
      cutright=match.group(4)

      # is there a synonym in parens?
      match = re.search(r"(\S+)\s+\((\w+)\)",cuttername)
      # yes
      if match:
        cutters[match.group(1)] = [cutleft,cutright]
        cutters[match.group(2)] = [cutleft,cutright]
      else:
        cutters[cuttername] = [cutleft,cutright]

# get user inputed enzyme info
cutParts = cutters[enzyme]
pattern = f"({cutParts[0]})({cutParts[1]})"
     

# find cut sites
for id in seqs:
   seq = seqs[id]
   print(f"========== {id} =============")
   if re.search(pattern,seq):
     carrots=re.sub(pattern,r"\1^\2",seq)
     fragments = carrots.split("^")
     frag_num = len(fragments)
     print (f"# {enzyme}: {frag_num} fragments")
     print (f"# Sequence annotated with cut sites")
     print(f">{id}\n{carrots}")
     print (f"# Fragments Natural Order")
     print(fragments)
     print (f"# Fragments Sorted by Length small->large")
     print(sorted(fragments,key=len))
   else:
     print (f"# {enzyme}: No Cut Sites Found")


    
