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

# create a dict to count up how many times we see the same PANTHER2GO term.
# create a dict to count up how many times we see the same InterPro2GO term.
# Some big picture questions to think about while coding.
# Is there a recurring GO term?
# Are the two sets of GO terms different?
# create a dict to count up how many times we see the same PFAM domain. 
# Is there a recurring domain?
panther2go   = {}
interpro2go  = {}
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

    ## Get Panther hits and PANTHER2GO terms
    # iprscan = { 'results' : [ {'matches': [ {'accession': 'PTHR0000'} ] }  , {'matches': [] } ] }
    if 'accession' in match:
      accession=match['accession']
      if accession.startswith('PTHR'):
        name=match['name']
        print(f"PNTHR: {accession} {name}")
     
        # now lets get the GO terms
        # Panther hits with associated GO terms have a key:value pair that is in the sub-dict 'goXRefs': [{},{}].
        # the value is a list of dictionaries that contains information about each go term.
        # get and store the info (id and name) about the go term 
        # iprscan = { 'results' : [ {'matches': [ {'accession': 'PTHR0000'} , {'goXRefs': [{'id': 'GO:0030182', 'name':'neuron differentiation'}] } ] }  , {'matches': [] } ] }
        for goXRef in match['goXRefs']:
          ## Replace the question marks with the appropriate keys
          go_id = goXRef['?'] # use goXRef as your dictionary, what key do you use to get id? 
          go_name =  goXRef['?'] # use goXRef as your dictionary, what key do you use to get name?
          goinfo=f"{go_id} {go_name}"
          print(f"\t{goinfo}")

          # lets count up each time we see each GO term hit across all of our sequences in our gene set
          if goinfo not in panther2go:
            panther2go[goinfo]=0
          panther2go[goinfo]+=1


    ## Get PFAM hits
    # Our sequences may have Pfam domain hits, they are stored in the sub-dict in 'signature' : {}
    # the value is a dictionary that contains information about each Pfam term
    # get and store the info (accession, name, and description) about the Pfam term 
    # iprscan = { 'results' : [ {'matches': [{'signature': {'accession' : 'PF03826' , 'description': 'OAR motif', 'name': 'OAR' }}] } ] }
    signature_accession = match['signature']['accession']
    if signature_accession.startswith('PF'):
      ## Replace the question marks with the appropriate keys
      name=match['signature']['?'] # what key do you use to get PFAM domain name?
      desc=match['signature']['?'] # what key do you use to get PFAM domain description
      pfaminfo=f"{signature_accession} {name} {desc}"
      print(f"PFAM: {pfaminfo}")

      # lets count up each time we see each pfam domain hit across all our sequences in our gene set
      if pfaminfo not in pfam:
        pfam[pfaminfo]=0
      pfam[pfaminfo]+=1

    ## Get InterPro2GO terms. 
    # Review the summary datastructure and the workshop notes to create this block to collect and count Interpro associated GO terms. 
    # the Panther2GO and Pfam code blocks are good models on how to write this block


    ## Get some other protein motif 
    # review your json to see if you can figure out how to add in another domain result
    # follow the format used for PFAM
    # add in a count, similar to the pfam domain counts and PANTHER2GO counts

print("\n")
print("Summary Cumulative Counts")
print("==== GO TERM Counts ===")
for info,count in sorted(panther2go.items(), key=lambda x:x[1], reverse=True):
  if count > 1:
    print(info,count)

## Add a counter for interpro2go using the above block as a model

print("\n")
print("==== PFAM Counts ===")
for info,count in sorted(pfam.items(), key=lambda x:x[1], reverse=True):
  if count > 1:
    print(info,count)
