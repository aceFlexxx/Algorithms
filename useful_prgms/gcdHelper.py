# An example of a recursive function to
# find the of two integers.

import math

def calc_gcd(x,y):
    """This is a recursive function
    to find the gcd of two integers"""
    quotient = int(math.floor(x/y))
    remainder = x%y
    if x%y == 0:
        print x, '=', y, ' * ', quotient, ' + ', remainder
        print "gcd is: ", y
        return
    else:
        print x, '=', y, ' * ', quotient, ' + ', remainder
        return (calc_gcd(y, remainder))

num1 = input("Enter first number for gcd:")
num2 = input("Now the second:")
if num1 < num2:
    holder = num2
    num2 = num1
    num1 = holder
print "The gcd of ", num1 ,"and" , num2, " -> \n"
calc_gcd(num1, num2)

