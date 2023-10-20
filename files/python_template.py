#!/usr/bin/env python3

# This script.... 
#
#

import argparse
# you need to install biopython for the next two imports to work
#from Bio import SeqIO
# from Bio import SeqFeature
import re
import os
import random
# need numpy and pandas installed for these
#import numpy as np
#import pandas as pd

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''
This script

''')
#add some arguments
parser.add_argument('-gb', required=True, help='Input Genbank filename', dest='infile')
parser.add_argument('-f', "-fasta", required=True, help='Output fasta filename', dest='outfile')
parser.add_argument('-type', help='extract protein or nucleotide sequence, required unless -genome', dest='type',
                    choices=['prot','nucl'])
parser.add_argument('-g' , '-genome', help = 'Just extract underlying genome sequence as fasta, defaults to nucl seq',
                    dest='genome',
                    action='store_true')
parser.add_argument('-debug', help ='Turn on debugging information', dest ='debug', action ='store_true')
# positional argument  (doesn't start with '--')
parser.add_argument('fastafile', help = 'the input fasta filename')
#parser.add_argument('fruits', help = 'Dummy list of fruits', nargs='*')

# parse command line
args = parser.parse_args()
debug = args.debug
fasta_file = args.fastafile
out_file = args.outfile



######################################################################
#####                FUNCTIONS                                 #######
######################################################################






######################################################################





######################################################################
#####                        MAIN                              #######
######################################################################




######################################################################






######################################################################





































































