#!/usr/bin/env python3
# ejr: 2023-10-16
# Eric's answer to problem set 7 question 10
import re
import sys

# first argument is enzyme anme
# second argument is the sequence name
# third argument is the fasta file name
# Sample command: ./Python_07_ejr_10.py AatII seq1 seq.nt.fa
def main():

    enzyme = sys.argv[1]
    seqname = sys.argv[2]
    fasta_dict = create_fasta_dict(sys.argv[3])
    enzyme_dict = create_enzyme_dict("bionet.txt")

    cut_seq(enzyme, fasta_dict[seqname], enzyme_dict)


# read in enzyme file and create dictionary
def create_enzyme_dict(filename):

    enzyme_file = open(filename, 'r')

    enzyme_dict = {}
    with enzyme_file as f:
        for line in enzyme_file:
        # discard lines that do not have a cut site specified
            if "^" in line:
                line = line.rstrip()
                matches = re.match(r'(.+?)\s{3,}(.+)', line)
                # some enzymes have more than one site in file
                # so we make a list

                # if there is no list of patterns yet, make one
                try:
                    len(enzyme_dict[matches.group(1)]) 
                except KeyError:
                    enzyme_dict[matches.group(1)] = []
                enzyme_dict[matches.group(1)].append(matches.group(2))

    return(enzyme_dict)

# read in fasta file and create dictionary
# I used a list instead of string appends because it is much faster
# when the sequence is very large (i.e. chromosomes)
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
    if enzyme in enzyme_dict:
        patterns = enzyme_dict[enzyme]
        print("Original Sequence: ", seq)
        # this is all to handle that there might be two cut patterns
        # so we add cut sites for each before we split.
        # this same type of loop would work for enzyme combinations
        for pattern in patterns:
            # convert ambiguous nucleotides to regex patterns
            pattern = re.sub('Y', '[TC]', pattern )
            pattern = re.sub('W', '[AT]', pattern)
            pattern = re.sub('N', '[ATGC]', pattern)
            pattern = re.sub('R', '[AG]', pattern)
            pattern = re.sub('K', '[GT]', pattern)
            pattern = re.sub('M', '[AC]', pattern)
            # first regex is used to set parenthesis in second regex
            #  to capture groups flanking ^ 
            regex = re.compile(r"(.*)\^(.*)")    
            regex2_string = re.sub(regex, r"(\1)(\2)", pattern)
            # second regex is used to put ^ into locations where pattern matches
            regex2 = re.compile(regex2_string)
            seq = re.sub(regex2, r"\1^\2", seq)    

        # split after all cuts
        seqs = seq.split("^")
        sorted_seqs = sorted(seqs, key = len, reverse=True)
        print("Annotated Sequence: ", seq)
        print("Number of Fragments: ", len(seqs))
        print("Fragments in natural order:\n"+ "\n".join(seqs))
        print("Fragments in sorted order:\n"+ "\n".join(sorted_seqs))

###############################################################################
### RUN MAIN ##################################################################
###############################################################################
if __name__ == "__main__":
    main()
