
# An example of a non-recursive function to
# calculate the Fibonacci Numbers.

import math
import time

def Fibo(n):
    """This is a recursive function
    to calculate the Fibinocci Numbers"""
    fLess2 = 0;
    fLess1= 1;
    fVal = fLess1 + fLess2
    for i in range(2, n+1):
        fVal = fLess1 + fLess2
        fLess2 = fLess1
        fLess1 = fVal
    return fVal
num1 = raw_input("Enter n for the Fibonacci #:")

if num1.isdigit() == False:
    num1 = 10000
else:
    num1 = int(num1)
start = time.time()
print  "The", num1," Fibonacci number in the sequence: \n", Fibo(num1)
end = time.time()

print "To calculate this with the improved algorithm,", \
    "It took me", 1000*(end - start), "msecs"
