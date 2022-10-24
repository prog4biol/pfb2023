#!/usr/bin/env python3

from Bio import SeqIO

filename = "../files/seq.nt.fa"

for seq_record in SeqIO.parse(filename, "fasta"):   
  print('ID',seq_record.id)
  print('len {}'.format(len(seq_record)))
  print('translation {}'.format(seq_record.seq.translate(to_stop=False)))
