#!/usr/bin/env python3
# ejr: 2022-10-16

import re
import sys

# first argument is enzyme anme
# second argument is the sequence name
# third argument is the fasta file name
def main():
	enzyme = sys.argv[1]
	seqname = sys.argv[2]
	enzyme_dict = create_enzyme_dict("bionet.txt")
	fasta_dict = create_fasta_dict(sys.argv[3])
	cut_seq(enzyme, fasta_dict[seqname], enzyme_dict)


# read in enzyme file and create dictionary
def create_enzyme_dict(filename):

	enzyme_file = open(filename, 'r')


	enzyme_dict = {}
	with enzyme_file as f:
		lines_after_10 = f.readlines()[10:]
		for line in lines_after_10:
			if len(line.strip()) != 0:
				line = line.rstrip()
				matches = re.match(r'(.+?)\s{3,}(.+)', line)
				#print(matches.group(0))
				if matches.group(1):
					enzyme_dict[matches.group(1)] = matches.group(2)
	return(enzyme_dict)

# read in fasta file and create dictionary
def create_fasta_dict(filename):
	header = ""
	fasta = {}

	fasta_file = open(filename, 'r')
	with fasta_file as fh:
		for line in fh:
			line = line.rstrip()
			if (line[0] == ">"):
				header = line[1:]
				fasta[header] = []
			else:
				fasta[header].append(line)
		for header in fasta:
			fasta[header] = ''.join(fasta[header])

	return fasta


def cut_seq(enzyme, seq, enzyme_dict):
#enzyme = "AatII"
#seq = "GACGTCGACGTCGGGG"
	if enzyme in enzyme_dict:
		pattern = enzyme_dict[enzyme]
		pattern = re.sub('Y', '[TC]', pattern )
		pattern = re.sub('W', '[AT]', pattern)
		pattern = re.sub('N', '[ATGC]', pattern)
		pattern = re.sub('R', '[AG]', pattern)
		pattern = re.sub('K', '[GT]', pattern)
		pattern = re.sub('M', '[AC]', pattern)
		regex = re.compile(r"(.*)\^(.*)")	
		regex2_string = re.sub(regex, r"(\1)(\2)", pattern)
		regex2 = re.compile(regex2_string)
		print("Original Sequence: ", seq)
		seq = re.sub(regex2, r"\1^\2", seq)	
		print("Sequence with sites: ", seq)
		seqs = seq.split("^")
		print("Number of Fragments: ", len(seqs))
		print("Fragments in natural order: ", seqs)
		seqs = sorted(seqs, key = len, reverse=True)
		print("Fragments in sorted order: ", seqs)

###############################################################################
### RUN MAIN ##################################################################
###############################################################################
if __name__ == "__main__":
	main()
