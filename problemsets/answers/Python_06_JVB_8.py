#!/usr/bin/env python3
# JVB 2022-10-17

# 8. Open the [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) file
#   [Python_06.fastq](https://raw.githubusercontent.com/prog4biol/pfb2022/master/files/Python_06.fastq) and
#   go through each line of the file. Count the number of lines and the number of characters per line. Have
#   your program report the:  
#     - total number of lines  
#     - total number of characters  
#     - average line length


# Because we want to get the total_line_count and total_char_count
# for the whole file, we have to define them above the loop (because
# we must iterate over every line contained in the file to examine
# the whole file)
total_line_count = 0
total_char_count = []
with open("Python_06.fastq", "r") as file_input:
    for line in file_input:
        line = line.rstrip()

        total_char_count.append(len(line))
        total_line_count += 1
        
print(f"Total number of lines: {total_line_count:d}")
print(f"Total number of characters: {sum(total_char_count):d}")
print(f"Average line length: {sum(total_char_count) / total_line_count:f}")
