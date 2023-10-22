#!/usr/bin/env python3
# ejr: 2023-10-18
# lmd: 2023-10-18
# Problem set 1 question 2

# replace occurances of old_name with new_name
import re

# set an incrementer to get line number
line_num=0
old_name="Nobody"
new_name="Tendo"

# open file
with open("Python_07_nobody.txt","r") as f_obj: 
	# iterate over each line in file, update line number, remove newline

	for line in f_obj:
		line = line.rstrip()

		# replace old_name with new_name
		new_line = re.sub(old_name, new_name, line)
		print(new_line)
