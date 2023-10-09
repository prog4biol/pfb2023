#!/usr/bin/env python3
# ejr: 2023-10-10
# pfb 2023: problem set python 2

import sys
number = sys.argv[1]

print(number)

# pos/neg test

if int(number) > 0:

	print("positive")
	if int(number) < 50:
		print("less than 50")
		if int(number) % 2 == 0:
			print("It is an even number that is smaller than 50")

	elif int(number) > 50:
		print("greater than 50")
		if int(number) % 3 == 0:	
			print("It is larger than 50 and divisible by 3")

	else:
		print("number is 50")

			
elif int(number) < 0:
	print("negative")
else:
	print("zero")

