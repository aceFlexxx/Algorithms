# A school method based Python3
# program to check if a number
# is prime

def isPrime(n):

    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True
num = input("Enter number to check for primality:")
# Driver Program to test above function
if isPrime(num):
    print("True")
else:
    print("false")

# This code is contributed by Smitha Dinesh Semwal
