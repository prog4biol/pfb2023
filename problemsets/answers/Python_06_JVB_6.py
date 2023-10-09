#!/usr/bin/env python3
# JVB 2023-10-17

# 6. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"

with open("Python_06.txt", "r") as file_input:
    with open("Python_06_uc.txt", "w") as file_output:
        for line in file_input:
            line = line.rstrip().upper()
            # since .rstrip() returns a new string,
            # we can chain on the .upper() method
            print(line, file=file_output)

        

