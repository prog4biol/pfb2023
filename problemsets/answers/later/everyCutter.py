#!/usr/bin/env python3
# regular expression cutter 
# by Sofia Robb

# search for every cut site found in the bionet collection in a user provided FASTA file
# report the sequence id, the enzyme name, the number of fragments, the average fragment length, the max and min fragment lengths


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
      seqs[id]+=line.upper()

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

      # replace degerate nucleotides with a regular expression character class
      degenerates = {
      # W	Weak	A/T
      'W' : '[AT]',
      # S	Strong	C/G
      'S' : '[CG]',
      # M	Amino	A/C
      'M' : '[AC]',
      # K	Keto	G/T
      'K' : '[GT]',
      # R	Purine	A/G
      'R' : '[AG]',
      # Y	Pyrimidine	C/T
      'Y' : '[CT]',
      # B	Not A	C/G/T
      'B' : '[CGT]',
      # D	Not C	A/G/T
      'H' : '[AGT]',
      # H	Not G	A/C/T
      'H' : '[ACT]',
      # V	Not T	A/C/G
      'V' : '[ACG]',
      # N	Any	A/C/G/T
      'N' : '[ACGT]'
      }
      for degen in degenerates:
         pattern = degenerates[degen]
         cutleft = cutleft.replace(degen,pattern)
         cutright = cutright.replace(degen,pattern)

     

      # is there a synonym in parens?
      match = re.search(r"(\S+)\s+\((\w+)\)",cuttername)
      # yes
      if match:
        cutters[match.group(1)] = [cutleft,cutright]
        cutters[match.group(2)] = [cutleft,cutright]
      else:
        cutters[cuttername] = [cutleft,cutright]

     

# find cut sites
print ('id','cutter','fragCount','averFragLen','maxFragLen','minFragLen',sep="\t")
for id in seqs:
   seq = seqs[id]
   for cutter in cutters:
     cutParts = cutters[cutter]
     pattern = f"({cutParts[0]})({cutParts[1]})"
     if re.search(pattern,seq):
       carrots=re.sub(pattern,r"\1^\2",seq)
       fragments = carrots.split("^")
       lengths = [len(frag) for frag in fragments]
       fragCount = len(fragments)
       maxFrag = max(lengths)
       minFrag = min(lengths)
       sumFrag = sum(lengths)
       averFrag = round(sumFrag/fragCount)
       print (id,cutter,fragCount,averFrag,maxFrag,minFrag,sep="\t")
     else:
       print (id,cutter,0,'N/A','N/A','N/A','N/A',sep="\t")


    
