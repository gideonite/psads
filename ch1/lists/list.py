#!/usr/bin/python

import random

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        '''
        self, item -> None.
        Adds the item to the front of the list.
        '''
        node = Node(item)
        node.setNext(self.head)

        if None == self.head:
            assert None == self.tail
            self.tail = node

        self.head = node

    def size(self):
        '''
        self -> int.
        Returns the number of nodes in the list.
        '''
        curr = self.head
        count = 0

        while curr != None:
            count += 1
            curr = curr.getNext()

        return count

    def search(self, item):
        '''
        self, item -> Boolean.
        Returns whether or not the item is in the list.
        '''
        curr = self.head

        while curr != None:
            if item == curr.getData():
                return True
            curr = curr.getNext()

        return False

    def remove(self, item):
        '''
        self, item -> None.
        Removes the item from the list.
        Assumes that the item is in the list.
        '''
        curr = self.head
        prev = None

        found = False
        while not found:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()

        if found:
            if None == prev:
                self.head = curr.getNext()
            else:
                prev.setNext(curr.getNext())

    def append(self, item):
        '''
        self, item -> None.
        Appends the item to the end of the list.
        And does so in constant algorithmic time.
        '''

        node = Node(item)

        if None == self.tail:
            self.add(node)

        self.tail.setNext(node)
        self.tail = node

    def index(self, item):
        '''
        self, item -> int.
        Returns the position (aka the index) of the item in the list.
        Assumes that the item is in the list.
        '''
        curr = self.head
        i = 0

        while None != curr:
            if item == curr.getData():
                return i

            i += 1
            curr = curr.getNext()

    def insert(self, i, item):
        '''
        self, i, item -> None.
        Adds the item to the list at index i.
        Assumes that i <= len(list).
        '''
        assert i >= 0
        node = Node(item)

        prev = None
        ith = self.head

        while i > 0:
            prev = ith
            ith = ith.getNext()
            i -= 1

        if None == prev:
            node.setNext(self.head)
            self.head = node
        else:
            node.setNext(ith)
            prev.setNext(node)

    def pop(self, i=None):
        '''
        self -> item (the last one in the list).
        self, i -> item (the ith item in the list).
        Either removes and returns the last item in the list or the ith item of the list.
        Assumes that there is a value at the given index.
        '''

        if None == i:
            prev = None
            curr = self.head

            while None != curr.getNext():
                prev = curr
                curr = curr.getNext()

            if None == prev:
                prev = self.head

            prev.setNext(None)

            return curr.getData()
        else:
            prev = None
            ith = self.head

            while i > 0:
                prev = ith
                ith = ith.getNext()
                i -= 1

            if None == prev:
                prev = self.head

            prev.setNext(ith.getNext())

            return ith.getData()



#
# TEST
#

def randomUnorderedList():
    ret = UnorderedList()
    for i in range(10):
        ret.add(random.choice(range(10)))

    return ret

list = UnorderedList()
assert list.isEmpty()
assert 0 == list.size()

list = UnorderedList()
list.add(42)
assert 1 == list.size()

list = randomUnorderedList()
list.add(42)
list.search(42)

list = randomUnorderedList()
list.add(42)
assert list.search(42)
list.remove(42)
assert not list.search(42)

list = UnorderedList()
list.append(10)
assert 0 == list.index(10)

list = UnorderedList()
list.append(0)
assert 0 == list.index(0)
list.append(1)
assert 1 == list.index(1)
list.append(2)
assert 2 == list.index(2)
assert 1 == list.index(1)
assert 0 == list.index(0)

list = randomUnorderedList()
list.insert(5, 420)
assert 5 == list.index(420)

list = UnorderedList()
list.insert(0, 12)
assert 0 == list.index(12)

list = UnorderedList()
list.add(10)
list.add(11)
assert 10 == list.pop()
assert 1 == list.size()

list = UnorderedList()
list.add(11)
list.add(10)
assert 11 == list.pop(1)
assert 10 == list.pop()