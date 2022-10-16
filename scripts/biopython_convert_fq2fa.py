#!/usr/bin/env python3

from Bio import SeqIO

count = SeqIO.convert('../files/pfb.fastq', 'fastq', '../files/pfb.converted.fa', 'fasta')

print("converted ", count, "fastq sequence records to fasta records")
