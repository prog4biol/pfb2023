#!/usr/bin/env python3
# JVB: 2023-10-12


# Problem 5:
#  Using a text editor, write a script that
#  
#  Assigns a value to a variable
#  Has a if/else statment in which:
#  It prints out a confirmation of truth if the value is true
#  It prints out "Not True" if the value is not true.


print("Problem 5:")
number = "my non-empty string"
if bool(number):
    print("True")
else:
    print("Not True")

    

# Problem 7:
#  Create a script that has a if/else statement that (remember to write a little bit at a time and test it)

#  Test to see if a number is positive or negative
#  print "positive" if it is positive
#  print "negative" if it is negative
#  save it and run it.
print("Problem 7:")

number = 15
if number >= 0:
    # I've opted to use `>=` here, even though this is not strictly correct,
    # because it just feels *more* wrong for "negative" to be printed when
    # number == 0. We almost never write `-0` when referring to the sign of 0,
    # but we do often write `0`, which could be analogous to write `1` when
    # we really mean `+1`.
    print("positive")
else:
    # if a number is not positive, it *must* be negative, so we use an `else`.
    print("negative")



# Problem 8:
#  Add an `elif` to test if the number is equal to 0. Save it and run it.
print("Problem 8:")

if number > 0:
    # now I use `>` here, as opposed to the `>=` above, because we are now
    # explicitly testing for 0 values.
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")



# Problem 9:
#  Add nested tests to your last script
#  
#  if it is positive, in addition to printing "positive"
#  test if it is smaller than 50
#  save it and run it
print("Problem 9:")

if number > 0:
    # now I use `>` here, as opposed to the `>=` above, because we are now
    # explicitly testing for 0 values.
    print("positive")
    if number < 50:
        # in order for us to reach this condition, we *must* have a positive
        # number, so we do not need to test both conditions in the same
        # conditional statement. i.e., we do *not* need to do:
        # if number > 0 and number < 50:
        #     print("positive")
        #     print("and smaller than 50")
        print("and smaller than 50")
elif number == 0:
    print("zero")

else:
    print("negative")

    

# Problem 10:
#  Add more nested tests to your script.
#
#  if it is smaller than 50
#  test if the number is even
#  if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
#  save it and run it
print("Problem 10:")
if number > 0:
    # now I use `>` here, as opposed to the `>=` above, because we are now
    # explicitly testing for 0 values.
    print("positive")
    if number < 50:
        if number % 2 == 0:
            # in order for us to reach this condition, we *must* have a positive
            # number, so we do not need to test both conditions in the same
            # conditional statement. i.e., we do *not* need to do:
            # if number < 50 and number % 2 == 0:
            #     # ...
            print("it is an even number that is smaller than 50")
elif number == 0:
    print("zero")

else:
    # The modulo operator returns the remainder from division `number / mod`.
    # All even values are divisible by 2, so using `number % 2` would be a
    # convenient way of approaching this problem. For all even values
    # `number % 2` returns 0, so we can leverage this fact. If we want odd
    # values, we can instead test for non-zero values.
    print("negative")


    
# Problem 11:
#  Add more nested tests.

#  if it is larger than 50,
#  test if the number is divisible by 3
#  if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"
#  save it and run it
print("Problem 11:")

if number > 0:
    # now I use `>` here, as opposed to the `>=` above, because we are now
    # explicitly testing for 0 values.
    print("positive")
    if number < 50:
        if number % 2 == 0:
            # in order for us to reach this condition, we *must* have a positive
            # number, so we do not need to test both conditions in the same
            # conditional statement. i.e., we do *not* need to do:
            # if number > 0 and number < 50:
            #     # ...
            print("it is an even number that is smaller than 50")
    elif number > 50:
        if number % 3 == 0:
            # same logic here as described for even values above.
            # if this statement is true, value must also be > 50, so no need to test
            # both conditions again.
            print("it is larger than 50 and divisible by 3")
            
elif number == 0:
    print("zero")
    
else:
    print("negative")

    

# Problem 12
#  In your previous nested tests, test the number 50. What prints to the screen?
#  Is it the correct response? If not, you have a semantic error and need to alter
#  your code to be correct with any number.

# When number == 50, the script written above will only print "positive" to the screen
# then exit.

print("Problem 12:")
number = 50
if number > 0:
    # now I use `>` here, as opposed to the `>=` above, because we are now
    # explicitly testing for 0 values.
    print("positive")
    if number < 50:
        if number % 2 == 0:
            # in order for us to reach this condition, we *must* have a positive
            # number, so we do not need to test both conditions in the same
            # conditional statement. i.e., we do *not* need to do:
            # if number > 0 and number < 50:
            #     # ...
            print("it is an even number that is smaller than 50")
    elif number > 50:
        if number % 3 == 0:
            # same logic here as described for even values above.
            # if this statement is true, value must also be > 50, so no need to test
            # both conditions again.
            print("it is larger than 50 and divisible by 3")
    else:
        # Since a number cannot be more than 50 and equal to 50, or less than 50 and
        # equal to 50, we can use an `else` here to catch when number == 50.
        print("equal to 50")
            
elif number == 0:
    print("zero")
    
else:
    print("negative")

