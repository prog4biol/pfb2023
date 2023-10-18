#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 1

# find every occurance of "Nobody" and print out the position
import re

# set an incrementer to get line number
line_num=0

# open file
with open("Python_07_nobody.txt","r") as f_obj: 
	# iterate over each line in file, update line number, remove newline
	for line in f_obj:
		line_num = line_num+1
		line = line.rstrip()

		# iterate over each match in the line
		for match in re.finditer("Nobody", line):
			start = match.start() + 1   # convert from 0 to 1 notation 
			end = match.end() 
			print(f"Line {line_num}: {start} - {end}")
