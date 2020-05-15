# An program trying out various
# quicksort implementations

import math
import numpy as np
import sys
import time


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def og_quick_sort(array, start, end):
    # This recursive function sorts an array via
    # the original 'vanilla' implementation"""

    if start >= end:
        return

    p = partition(array, start, end)
    og_quick_sort(array, start, p-1)
    og_quick_sort(array, p+1, end)

def dispArray(array):
    counter = 0;
    for i in range(0 , len(array)):
        sys.stdout.write("%s" % array[i])
        if (i%20 == 0 or i == len(array)-1) and i != 0:
            sys.stdout.write('\n')
        else:
            sys.stdout.write(',')

low = 1
high = 1001
size = 1000



list1 = np.random.randint(low, high, size)
list2 = [i for i in range(1,1000)]
list3 = list2.reverse()

dispArray(list1)

