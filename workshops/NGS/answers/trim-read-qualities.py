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
    # "infile.fastq", not "<infile.fastq>"
    stream.write(f"""
Usage: {program} <input.fastq> <min-qual>

{message}""")

    # Return an exit status reflective of whether the code 
    # execution resulted in an error (> 0) or not (= 0):
    sys.exit(status)



def trim_reads_from_fileobj(min_quality_threshold=-1, infile=sys.stdin, outfile=sys.stdout):
    # This function is the core of our script. FASTQ files *always*
    # have four lines per record, so we will iterate over the file
    # four lines at a time using a `for` loop and the next() function
    # (to pull out second, third, and fourth lines in a single loop):

    for header in infile:  # this line *always* pulls the first (header)
        # call next() on the *SAME* fileobj to pull out another
        # line to get the sequence string
        nucleotides = next(infile)
        # call next() on the *SAME* fileobj to pull out another
        # line to get `+` line
        plussign  = next(infile)
        # call next() on the *SAME* fileobj to get out another
        # line to get the quality string
        qualities = next(infile)

        # remove newline (`\n`) chars from the input strings:
        header = header.rstrip()
        nucleotides = nucleotides.rstrip()
        plussign = plussign.rstrip()
        qualities = qualities.rstrip()

        # The exercise question prompts us to iterate backward
        # over the string until we encounter a quality value
        # that exceeds our minimum quality threshold. The `~`
        # operator gives us the corresponding index starting
        # from the *end* of the sequence:
        #  i => ~i
        #  0    -1
        #  1    -2
        #  2    -3
        #  ...
        #  n    -(n + 1)
        for index in range(len(nucleotides)):
            # strings can be thought of abstractly as "lists"
            # of characters, so use the index to get a single
            # quality character to calculate the quality value:
            quality_char = qualities[~index]

            # Nearly all modern/recent FASTQ files come encoded
            # as Phred 33 offset, so convert our quality char
            # to its corresponding ASCII ordinal value, then
            # subtract the offset to get the quality score:
            quality_score = ord(quality_char) - 33

            # when we encounter a quality score above our minimum
            # threshold, stop this loop
            if quality_score >= min_quality_threshold:
                break

        # because python has weak scope, we can use the last-
        # encountered index from the above `for` loop as the
        # trim position. It is entirely possible that an entire
        # read can be low quality and we can replace the record
        # with a "null" record (nucleotides="N", qualities="!").
        # When this happens, index == len(nucleotides)-1.
        if index == len(nucleotides) - 1:
            # The whole read is trash, set nucleotides to 'N' and
            # qualities to '!' (i.e., quality_score == 0 in Phred 33)
            nucleotides = 'N'
            qualities = '!'
        else:
            # Given that we have identified where our qualities
            # exceed the min_quality_threshold, now trim the ends
            # using the same `~` char trick on index using string
            # slice notation (take everything from start of string
            # up to ~index):
            nucleotides = nucleotides[:~index]
            qualities = qualities[:~index]

        # with the print() function, assign the `file` keyword arg
        # to specify which file object to print to:
        print(header, file=outfile)
        print(nucleotides, file=outfile)
        print(plussign, file=outfile)
        print(qualities, file=outfile)

        # since this function is reading and writing to files,
        # there is no need to use a `return`, which we only use
        # to output data from our function.
        

def main(arguments):
    # In programming style, the main() function is where command-line inputs
    # are handled and the usage message is emitted when the user gives bad
    # input arguments. Once our script validates it is happy with its inputs,
    # proceed to call the core script function: trim_reads_from_file()

    
    if len(arguments) == 0:
        # If the user gives no arguments, print the usage synopsis nicely:
        usage(status=0)
        
    elif len(arguments) != 2:
        # If the user gives too few or too many arguments, complain loudly:
        usage(
            message="Unexpected number of arguments",
            status=1
        )

    # Attempt to open a fastq file for reading:
    ifastq = open(arguments[0], 'r')

    # We want to print to the screen (which python does by default), but
    # we can build in some flexibility by coding in handling an output
    # file variable explicitly:
    ofastq = sys.stdout

    # The second argument to our script *should* be an integer, but if the
    # user provides, say, a string, then we should catch the error gracefully
    # and tell the user nicely that we expect an integer instead:
    try:
        # Calling int() raises a ValueError if it cannot convert our
        # input arguments[1] (which is a string from sys.argv) into
        # an integer:
        min_quality_threshold = int(arguments[1])
    except ValueError:
        usage(
            message="<min-qual> argument must be an integer",
            status=1
        )

    trim_reads_from_fileobj(min_quality_threshold, ifastq, ofastq)

    # finally, when working with files, close your files explicitly:
    ifastq.close()
    ofastq.close()


if __name__ == '__main__':
    main(sys.argv[1:])
