#!/usr/bin/env python3

# import the os module to trim off the file path off the of
# the script name (to get the path "basename").
import os

# import sys to take positional arguments from the command
# line
import sys

# I like to build these usage functions that allow me to print
# the same command line usage synopsys under different input
# conditions:
def usage(message=None, status=1, stream=sys.stderr):
    # another way to get the program name:
    program = os.path.basename(__file__)

    # format a pretty usage message to help the user learn
    # how to run your code. The more user-friendly your code
    # is, the more likely others are to use it
    message = '' if message is None else f'ERROR: {message}\n\n'

    # In programming convention arguments with <> around them
    # denote *required* arguments, while [] denote *optional*
    # arguments, and does not mean those characters need to be
    # included in the file name: i.e., the user should input
    # "infile.depth", not "<infile.depth>"
    stream.write(f"""
Usage: {program} <input.tsv>

{message}""")

    # Return an exit status reflective of whether the code 
    # execution resulted in an error (> 0) or not (= 0):
    sys.exit(status)



def parse_INFO_to_dict(info_string):
    info_keyval_pairs = info_string.split(';')
    info_dict = {}
    for keyval in info_keyval_pairs:
        (key, value) = keyval.split('=', maxsplit=1)
        info_dict[key] = value

    return info_dict
    


def parse_sample_to_dict(format_string, sample_string):
    return dict(zip(format_string.split(':'), sample_string.split(':')))



def calc_Zscore(x, mean, sd):
    return((x - mean) / sd)


def extract_csq_info_from_file(infile=sys.stdin):

    bcsq = []
    for line in infile:
        line = line.strip()
        
        if line.startswith('#'):
            continue

        fields = line.split("\t")

        if len(fields) < 10:
            # our VCF has no Sample field
            continue

        sample = parse_sample_to_dict(fields[8], fields[9])
        info = parse_INFO_to_dict(fields[7])
        
        if sample['GT'].startswith("0"):
            # our sample isn't variant at this position
            continue

        if 'BCSQ' in info:
            if 'frameshift' in info['BCSQ']:
                bcsq.append((fields[0], fields[1], int(sample['DP']), info['BCSQ']))
    return bcsq


            
def main(arguments):
    # In programming convention, the main() function is where command-line
    # inputs are handled and the usage message is emitted when the user gives
    # bad input arguments. Once our script validates it is happy with its
    # inputs, proceed to call the core script function:
    # extract_csq_info_from_file()
    if len(arguments) == 0:
        # If the user gives no arguments, print the usage synopsis nicely:
        usage(status=0)
        
    elif len(arguments) != 3:
        # If the user gives too few or too many arguments, complain loudly:
        usage(
            message="Unexpected number of arguments",
            status=1
        )

    filename = arguments[0]
    # Attempt to open a fastq file for reading:
    vcf_file = open(filename, 'r')

    # We want to print to the screen (which python does by default), but
    # we can build in some flexibility by coding in handling an output
    # file variable explicitly:
    ostats = sys.stdout

    try:
        mean = float(sys.argv[2])
        sd = float(sys.argv[3])
    except ValueError:
        usage("Expected floating point value")
    
    bcsq = extract_csq_info_from_file(vcf_file)

    # the output fields (in order) are: 
    print(
        "\t".join((
            "chr",
            "pos",
            "depth_zscore",
            "effect",
            "gene_symbol",
            "gene_id",
            "coding_status",
            "gene_strand",
            "mutation_peptide",
            "mutation_nucleotide"
        ))
    )
    for chr, pos, dp, info in bcsq:
        zscore = calc_Zscore(dp, mean, sd)
        info = info.replace("|","\t")
        print(f"{chr}\t{pos}\t{zscore}\t{info}", file=ostats)
    
    # finally, when working with files, close your files explicitly:
    vcf_file.close()
    ostats.close()


if __name__ == '__main__':
    main(sys.argv[1:])
