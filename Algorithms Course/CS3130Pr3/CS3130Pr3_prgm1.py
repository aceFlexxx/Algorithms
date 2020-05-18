
# An program trying out various
# quicksort implementations

import math
import numpy as np
import sys
import time
import random
import heapq


'''
This function utilizes python's heapq obj.
In class we use a max heap, but this not the case
for heapq. For this reason, classes are created
to easily convert to max heap.

'''

class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)

class MinHeap(object):
    def __init__(self):
        self.h = []
        self.que = 0
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def heappush(self,x):
        if(len(MinHeap) + 1 > self.que):

        heapq.heappush(self.h,MaxHeapObj(x))
        self.que = self.que + 1

    def heappop(self):
        self.que = self.que - 1
        return heapq.heappop(self.h).val
    def __getitem__(self,i): return self.h[i].val
    def __len__(self): return len(self.h)

def disp_array(array):
    counter = 0;
    for i in range(0 , len(array)-1):
        sys.stdout.write("%s" % array[i])
        if (i%20 == 0) and i != 0 :
            sys.stdout.write('\n')
        elif (i%20 == 0 ) and i !=0:

            sys.stdout.write('\n')
        else:
            sys.stdout.write(',')


#copies an array to a heap
def array_to_heap(array):
    maxh = MaxHeap()
    for x in array:
        maxh.heappush(x)
    return maxh

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
size = 2000
high = size + 1

arr1 = np.random.randint(low, high, size)
arr1 = np.arr1(arr1)

minh = MinHeap()
maxh = heapq.heapify(arr.tolist())
# fetch "top" values
print(maxh[0])
print(len(maxh))
# fetch and remove "top" values
