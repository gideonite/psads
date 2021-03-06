#!/usr/bin/python

import math

class MaxHeap:
    '''
    Implements a max heap. Should be similar for a min heap.

    A heap encapsulates an array. A node in the heap is represented by an index
    `i`. The left and right children of `i` are `2 * i` and `2 * i + 1`
    respectively, or `None` if the node is a leaf.
    '''
    root = 0 # zero indexed

    def __init__(self, array=[]):
        self.array = array
        self.heap_size = len(array)

    def parent(self, i):
        '''
        Returns the parent of `i`.
        '''

        if 0 == i or i > self.heap_size:
            return None

        return (i-1)/2

        return i/2

    def left(self, i):
        '''
        Returns the left child of `i` or None if `i` is a leaf.
        '''
        l =  2 * i + 1
        if l >= self.heap_size:
            return None
        return l

    def right(self, i):
        '''
        Returns the right child of `i` or None if `i` is a leaf.
        '''
        r = 2 * i + 1
        if r >= self.heap_size:
            return None
        return r

    def get(self, i):
        '''
        Looks up the value of the node `i`.
        '''
        return self.array[i]

    def recursive_max_heapify(self, i):
        '''
        Float node `i` down until the heap property is met:
            Heap[Parent[i]] >= Heap[i]
        '''
        curr = self.array[i]
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l and self.array[l] > curr:
            largest = l

        # if both node < left and node < right, prefer the right child
        if r and self.array[r] > curr:
            largest = r

        if i != largest:
            # swap
            self.array[i] = self.array[largest]
            self.array[largest] = curr

            # float to the next one
            self.recursive_max_heapify(largest)

    def iterative_max_heapify(self, i):
        curr = i
        largest = None

        while 1:
            curr_val = self.array[curr]
            l = self.left(curr)
            r = self.right(curr)

            if l and self.array[l] > curr_val:
                largest = l

            if r and self.array[r] > curr_val:
                largest = r

            if curr == largest:
                break

            # swap
            self.array[curr] = self.array[largest]
            self.array[largest] = curr_val

            curr = largest

h1 = MaxHeap([2,3,1])

h2 = MaxHeap([-1] + range(100,-1,-1))
h2prime =  Heap([-1] + range(100,-1,-1))

h2.recursive_max_heapify(0)
h2prime.iterative_max_heapify(0)
assert h2.array == h2prime.array
