#!/usr/bin/env python3

import json
import sys
from pprint import pprint
from Bio import SeqIO

fastafile = sys.argv[1]
jsonfile = sys.argv[2]

# parse FASTA and create a dictionary with
# key = sequence and value = seq id
# iprscan uses the actual sequence as a unique identifier, and not the seq id
# we will make a dict that we can use to map the sequence to the id
seqs={}
for seq_record in SeqIO.parse(fastafile, "fasta"):
  fasta_seq=str(seq_record.seq)
  fasta_seq=fasta_seq.replace('*','')
  if fasta_seq == 'Sequence unavailable':
    continue
  seqs[fasta_seq]={}
  seqs[fasta_seq]['id']=seq_record.id
  seqs[fasta_seq]['desc']=seq_record.description

# read IPRSCAN json file
with open(jsonfile, 'r') as myfile:
    data=myfile.read()

# create a dict to count up how many times we see the same PANTR2GO term.
# Is there a recurring GO term?
# create a dict to count up how many times we see the same PFAM domain. 
# Is there a recurring domain?
go   = {}
pfam = {}

# parse iprscan json file
# create a dictionary from the json
iprscan = json.loads(data)

# iprscan is a dict with a key called 'results
# the value of results is a list of dictionaries 
# iprscan = { 'results' : [ {} , {} ] }
for result in iprscan['results']:

  # iprscan uses the seq as a uniq identifier, lets use the FASTA to map back to seq id
  sequence=result['sequence']
  if sequence == 'SEQUENCEUNAVAILABLE':
    continue
  seqid = seqs[sequence]['id']
  seqdesc = seqs[sequence]['desc']


  # Print a line to separate records
  print("=============")
  print(seqid,seqdesc,"\n")
 
  # iprscan = { 'results' : [ {'matches': [] } , {'matches': [] } ] }
  # each element of 'results' value list is a dictionary.
  # this dictionary has a key called 'matches' 
  # 'matches' value is list
  # 'matches' : []
  for match in result['matches']:

    ## Get Panther hits and PNTHR GO terms
    # iprscan = { 'results' : [ {'matches': [ {'accession': 'PTHR0000'} ] }  , {'matches': [] } ] }
    if 'accession' in match:
      accession=match['accession']
      if accession.startswith('PTHR'):
        name=match['name']
        print(f"PNTHR: {accession} {name}")
     
        # now lets get the GO terms
        # Panther hits with associated GO terms have a key:value pair that is 'goXRefs': {}.
        # the value is a dictionary that contains information about each go term.
        # get the info about the go term 
        # iprscan = { 'results' : [ {'matches': [ {'accession': 'PTHR0000'} , {'goXRefs': {'id': 'GO:0030182', 'name':'neuron differentiation'} } ] }  , {'matches': [] } ] }
        for goXRef in match['goXRefs']:
          go_id = goXRef['?'] # use goXRef as your dictionary, what key do you use to get id? 
          go_name =  goXRef['?'] # use goXRef as your dictionary, what key do you use to get name?
          goinfo=f"{go_id} {go_name}"
          print(f"\t{goinfo}")

          # lets count up each time we see each GO term hit on our sequences
          if goinfo not in go:
            go[goinfo]=0
          go[goinfo]+=1

    ## Get PFAM hits
    # iprscan = { 'results' : [ {'matches': [{'signature': {'accession' : 'PF03826' , 'description': 'OAR motif', 'name': 'OAR' }}] } ] }
    signature_accession = match['signature']['accession']
    if signature_accession.startswith('PF'):
      name=match['signature']['?'] # what key do you use to get PFAM domain name?
      desc=match['signature']['?'] # what key do you use to get PFAM domain description
      pfaminfo=f"{signature_accession} {name} {desc}"
      print(f"PFAM: {pfaminfo}")

      # lets count up each time we see each pfam domain hit on our sequences
      if pfaminfo not in pfam:
        pfam[pfaminfo]=0
      pfam[pfaminfo]+=1


    ## Get some other protein motif 
    # review your json to see if you can figure out how to add in another type of domain result
    # also add in a count like we did with pfam domain counts and PNTHR2GO counts

print("\n")
print("Summary Cumulative Counts")
print("==== GO TERM Counts ===")
for info,count in sorted(go.items(), key=lambda x:x[1], reverse=True):
  if count > 1:
    print(info,count)

print("\n")
print("==== PFAM Counts ===")
for info,count in sorted(pfam.items(), key=lambda x:x[1], reverse=True):
  if count > 1:
    print(info,count)
