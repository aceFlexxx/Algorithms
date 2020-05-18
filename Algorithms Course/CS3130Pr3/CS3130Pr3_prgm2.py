import sys
import math
import numpy as np
import sys
import time
import random

class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
        self._locked = True

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def maxHeapify(self, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap this is where
    # the most work was done to the given code.
    # Originally it would just ignore insertion if it was
    # out of bounds.
    def insert(self, element):
        if self.size >= self.maxsize:
            print("\nBefore change: " + str(self.size))
            newHeap = MaxHeap(2*self.maxsize)
            print("After change: " + str(newHeap.maxsize) +  "\n")
            for x in range(1, self.size + 1):
                newHeap.insert(self.Heap[x])

            newHeap.size += 1
            newHeap.Heap[newHeap.size] = element


            current = newHeap.size

            while newHeap.Heap[current] > newHeap.Heap[newHeap.parent(current)]:
                newHeap.swap(current, newHeap.parent(current))
                current = newHeap.parent(current)

            self.size = newHeap.size
            self.Heap = newHeap.Heap
            self.maxsize = newHeap.maxsize
        else:
            self.size+= 1
            self.Heap[self.size] = element


            current = self.size


            while self.Heap[current] > self.Heap[self.parent(current)]:
                self.swap(current, self.parent(current))
                current = self.parent(current)

    # Function to print the contents of the heap

    def Print(self):

    #    for i in range(1, (self.size//2)+1):
    #        print(" PARENT : "+str(self.Heap[i])+" LEFT CHILD : "+
    #                           str(self.Heap[2 * i])+" RIGHT CHILD : "+
    #                           str(self.Heap[2 * i + 1]))
        for i in range(1 , self.size):
            sys.stdout.write("%s" % self.Heap[i])
            if (i%20 == 0):
                sys.stdout.write('\n')
            elif i >= self.size - 1:
                sys.stdout.write('\n')
            else:
                sys.stdout.write(',')


    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.maxHeapify(self.FRONT)
        return popped

def dispArray(array):
    for j  in range(0 , len(array)-1):
        sys.stdout.write("%s" % array[j])
        if(((j+1)%20 == 0) and (j != 0)) or j + 1 == len(array) - 1:
            sys.stdout.write('\n')
        else:
            sys.stdout.write(',')

# Driver Code
if __name__ == "__main__":
    low = 1
    array_size = 101
    max_array_size = 2000
    high = max_array_size + 1


    heap = MaxHeap(100)
    counter = 0
    other = 0
    for j in range(0, max_array_size/(array_size - 1)):

        list1 = np.random.randint(low, high, array_size - 1)
        print("Data to be inserted:\n")
        dispArray(list1)
        print("\n")
        for i in range(0,array_size - 1):
            heap.insert(list1[i])
            other += 1
        counter += 1

#    heap.Print()
    list2 = [0]*heap.size
    for j in range(0, heap.size - 1):
        list2[j] = heap.extractMax()
print("The heap sorted array: \n")
dispArray(list2)
