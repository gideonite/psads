#!/usr/bin/python

class PQueue:
    def __init__(self, compare):
        self.compare = compare
        self.array = []

    def size():
        return len(self.array)

    def push(item):
        return item

    def pop():
        return self.array.pop()

def median(iterator):

    med = 0
    minheap = PQueue(lambda x,y: x < y)
    maxheap = PQueue(lambda x,y: x > y)

    while iterator.hasNext():
        anext = iterator.next()

        if anext <= med:
            minheap.push(anext)
        else:
            maxheap.push(anext)

        if minheap.size() > maxheap.size():
            med = minheap.pop()
        else:
            med = maxheap.pop()

    return med