# Python3 program to Find Number of digits
# in base b.

import math

# function to print number of
# digits
def findNumberOfDigits(n, base):

    # Calculating log using base
    # changing property and then
    # taking it floor and then
    # adding 1.
    dig = (math.floor(math.log(n) /
                 math.log(base)) + 1)

    # printing output
    print ("The Number of digits of"
      " Number {} in base {} is {}"
            . format(n, base, dig))

# Driver method

# taking inputs

n = input("Enter number to check for digit count:")
base = input("Enter base to check for digit count:")

# calling the method
findNumberOfDigits(n, base)

# This code is contributed by
# Manish Shaw (manishshaw1)
