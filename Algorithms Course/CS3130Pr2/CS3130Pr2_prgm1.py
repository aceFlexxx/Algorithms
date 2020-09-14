    # An program trying out various
    # quicksort implementations

    import math
    import numpy as np
    import sys
    import time
    import random


    '''
    This function takes the first element as pivot,
    places the pivot element at the correct position
    in the sorted array. All the elements are re-arranged
    according to the pivot, the elements smaller than the
    pivot is places on the left and the elements
    greater than the pivot is placed to the right of pivot.
    '''
    '''
    This function takes the first element as pivot,
    places the pivot element at the correct position
    in the sorted array. All the elements are re-arranged
    according to the pivot, the elements smaller than the
    pivot is places on the left and the elements
    greater than the pivot is placed to the right of pivot.
    '''

    swaps = 0
    comps = 0
    og_swaps = 0
    rando_swaps = 0
    three_swaps = 0

    og_comps = 0
    rando_comps = 0
    three_comps = 0

    def partition(arr,start,stop):
        global comps

        pivot = start # pivot
        i = start + 1 # a variable to memorize where the
                      # partition in the array starts from.
        for j in range(start + 1, stop + 1):

            # if the current element is smaller or equal to pivot,
            # shift it to the left side of the partition.
            if arr[j] <= arr[pivot]:
                swap(arr, i, j)
                #arr[i] , arr[j] = arr[j] , arr[i]
                i = i + 1
            else:
                comps = comps + 1
        arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
        pivot = i - 1
        return (pivot)


    # This function generates random pivot, swaps the first
    # element with the pivot and calls the partition fucntion.
    def partition_rand(array , start, end):

        # Generating a random number between the
        # starting index of the array and the
        # ending index of the array.
        rand_pivot = random.randrange(start, end)

        # Swapping the starting element of the array and the pivot
        array[start], array[rand_pivot] = array[rand_pivot], array[start]
        return partition(array, start, end)

    def find_median(a, b, c):
        if (a - b)*(c - a) >= 0:
            return a
        elif (b - a)*(c - b) >= 0:
            return b
        else:
            return c


    def swap(array,a,b):
        global swaps
        global comps

    array[a],array[b] = array[b],array[a]
    swaps = swaps + 1
    comps = comps + 1


def median_partition(array, start, end):
    median = (end - 1 - start) / 2
    median = median + start
    left = start + 1
    if (array[median] - array[end - 1])*(array[start] - array[median]) >= 0:
        array[start], array[median] = array[median], array[start]
    elif (array[end - 1] - array[median])*(array[start] - array[end - 1]) >= 0:
        array[start], array[end - 1] = array[end - 1], array[start]
    pivot = array[start]

    for right in range(start,end):
        if pivot > array[right]:
            swap(array,left,right)
            left = left + 1
    swap(array,start,left-1)
    return left-1



def og_quicksort(array, start, end):
    # This recursive function sorts an array via
    # the original 'vanilla' quick_sort implementation"""

    if start >= end:
        return

    pivot_index = partition(array, start, end)
    og_quicksort(array, start, pivot_index - 1)
    og_quicksort(array, pivot_index + 1, end)
    return array

# The function implements QuickSort
# using the random partition tech.

def random_quicksort(array, start , end):
    if(start < end):

        # pivotindex is the index where
        # the pivot lies in the array
        pivot_index = partition_rand(array, start, end)

        # At this stage the array is partially sorted
        # around the pivot. Separately sorting the
        # left half of the array and the right half of the array.
        random_quicksort(array , start , pivot_index - 1)
        random_quicksort(array, pivot_index + 1, end)
        return array


def median_quicksort(array,start,end):
    if start < end:
        split_point = median_partition(array,start,end)
        median_quicksort(array,start,split_point)
        median_quicksort(array,split_point+1,end)
        return array

def dispArray(array):
    counter = 0;
    for i in range(0 , len(array)-1):
        sys.stdout.write("%s" % array[i])
        if (i%20 == 0) and i != 0 :
            sys.stdout.write('\n')
        elif (i%20 == 0 ) and i !=0:

            sys.stdout.write('\n')
        else:
            sys.stdout.write(',')
def init_counters(swap_counter, comp_counter):
    # saves counters and inititializes them
    global swaps
    global comps

    swap_counter = swaps
    swaps = 0
    comp_counter = comps
    comps = 0

    return swap_counter, comp_counter


low = 1
size = 1000
high = size + 1




list1 = np.random.randint(low, high, size)
list2 = [i for i in range(1,size)]
list3 = list2[::-1]


dispArray(list1)


# First list
start = time.time()

list1_sorted = og_quicksort(list1, 0, len(list1) - 1)

end = time.time()

og_swaps, og_comps = init_counters(og_swaps, og_comps)

og_time = 1000*(end - start)
print "\n To calculate this with the original algorithm,", \
        "It took me", og_time, "msecs, ", og_swaps, " swaps, ",\
        "and", og_comps, " comparisons."
print  "The sorted list using the original algorithm: \n", dispArray(list1_sorted)


start = time.time()

list1_sorted = random_quicksort(list1, 0, len(list1) - 1)

end = time.time()

rando_swaps, rando_comps = init_counters(rando_swaps, rando_comps)

rand_time = 1000*(end - start)

print "To calculate this with the random algorithm,", \
    "It took me", rand_time, "msecs, ", rando_swaps, " swaps, ",\
        "and", rando_comps, " comparisons."
print  "The sorted list using the random sort: \n", dispArray(list1_sorted)


start = time.time()

list1_sorted = median_quicksort(list1, 0, len(list1) - 1)

end = time.time()

three_swaps, three_comps = init_counters(three_swaps, three_comps)

median_time = 1000*(end - start)
print "To calculate this with the median algorithm,", \
    "It took me", median_time, "msecs, ", three_swaps, " swaps, ",\
        "and", three_comps, " comparisons."
print  "The sorted list using the median sort: \n", dispArray(list1_sorted)


# Second list

start = time.time()

list2_sorted = og_quicksort(list2, 0, len(list2) - 1)

end = time.time()

og_swaps, og_comps = init_counters(og_swaps, og_comps)

og_time = 1000*(end - start)
print "To calculate this with the original algorithm,", \
        "It took me", og_time, "msecs, ", og_swaps, " swaps, ",\
        "and", og_comps, " comparisons."
print  "The sorted list using the original algorithm: \n", dispArray(list1_sorted)


start = time.time()

list2_sorted = random_quicksort(list2, 0, len(list2) - 1)

end = time.time()

rando_swaps, rando_comps = init_counters(rando_swaps, rando_comps)

rand_time = 1000*(end - start)

print "To calculate this with the random algorithm,", \
    "It took me", rand_time, "msecs, ", rando_swaps, " swaps, ",\
        "and", rando_comps, " comparisons."
print  "The sorted list using the random sort: \n", dispArray(list1_sorted)


start = time.time()

list2_sorted = median_quicksort(list2, 0, len(list2) - 1)

end = time.time()

three_swaps, three_comps = init_counters(three_swaps, three_comps)

median_time = 1000*(end - start)
print "To calculate this with the median algorithm,", \
    "It took me", median_time, "msecs, ", three_swaps, " swaps, ",\
        "and", three_comps, " comparisons."
print  "The sorted list using the median sort: \n", dispArray(list1_sorted)

# Third list

start = time.time()

list3_sorted = og_quicksort(list3, 0, len(list3) - 1)

end = time.time()

og_swaps, og_comps = init_counters(og_swaps, og_comps)

og_time = 1000*(end - start)
print "To calculate this with the original algorithm,", \
        "It took me", og_time, "msecs, ", og_swaps, " swaps, ",\
        "and", og_comps, " comparisons."
print  "The sorted list using the original algorithm: \n", dispArray(list1_sorted)


start = time.time()

list3_sorted = random_quicksort(list3, 0, len(list3) - 1)

end = time.time()

rando_swaps, rando_comps = init_counters(rando_swaps, rando_comps)

rand_time = 1000*(end - start)

print "To calculate this with the random algorithm,", \
    "It took me", rand_time, "msecs, ", rando_swaps, " swaps, ",\
        "and", rando_comps, " comparisons."
print  "The sorted list using the random sort: \n", dispArray(list1_sorted)


start = time.time()

list3_sorted = median_quicksort(list3, 0, len(list3) - 1)

end = time.time()

three_swaps, three_comps = init_counters(three_swaps, three_comps)

median_time = 1000*(end - start)
print "To calculate this with the median algorithm,", \
    "It took me", median_time, "msecs, ", three_swaps, " swaps, ",\
        "and", three_comps, " comparisons."
print  "The sorted list using the median sort: \n", dispArray(list1_sorted)
