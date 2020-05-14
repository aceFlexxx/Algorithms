# An example of a recursive function to
# calculate the Fibonacci Numbers.

import math
import time

def Fibo(n):
    """This is a recursive function
    to calculate the Fibinocci Numbers"""

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

num1 = raw_input("Enter n for the Fibonacci #:")

if num1.isdigit() == False:
    num1 = 41
else:
    num1 = int(num1)
start = time.time()
print  "The", num1," Fibonacci number in the sequence: \n", Fibo(num1)
end = time.time()

print "To calculate this with the Fn = Fn-1 + Fn-2 formula,", \
    "Python does not have an overflow problem. It took me", end - start, "secs"
