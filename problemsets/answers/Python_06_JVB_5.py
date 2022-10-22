#!/usr/bin/env python3
# JVB 2022-10-17

# 5. Write a script to do the following to [Python_06.txt](https://raw.githubusercontent.com/prog4biol/pfb2022/master/files/Python_06.txt)
#    - Open and read the contents.  
#    - Uppercase each line
#    - Print each line to the STDOUT

with open("Python_06.txt", "r") as file_input:
    for line in file_input:
        line = line.rstrip().upper()
        # since .rstrip() returns a new string,
        # we can chain on the .upper() method
        print(line)

