#!/usr/bin/python

class Node:
    def __init__(self,initdata):
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

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def size(self):
        curr = self.head
        count = 0

        while curr != None:
            count += 1
            curr = curr.getNext()

        return count

    def search(self, item):
        curr = self.head

        while curr != None:
            if item == curr.getData():
                return True
            curr = curr.getNext()

        return False

    def remove(self, item):
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

    def append(self,item):
        curr = self.head
        prev = None
        node = Node(item)

        while curr != None:
            prev = curr
            curr = curr.getNext()

        if None == prev:
            self.head = node
        else:
            prev.setNext(node)

    def insert(self,i,item):
        curr = self.head
        prev = None
        node = Node(item)

        while curr != None or i > 0:
            prev = curr
            curr = curr.getNext()
            i -= 1

        if None == prev:
            node.setNext(self.head)
            self.head = node
        else:
            node.setNext(curr)
            prev.setNext(node)

    def index(self,item):
        ITEM_NOT_FOUND = -1

        curr = self.head
        i = ITEM_NOT_FOUND

        found = False
        while None != curr and not found:
            if item == curr.getData():
                found = True

            i += 1
            curr == curr.getNext()

        return i

#insert, index, and pop

#
# TEST
#

list = UnorderedList()

assert list.isEmpty()

list.add(1) # [1]
assert list.search(1)
assert not list.search(2)

list.remove(1) # []
assert not list.search(1)

list.append(42) # [42]
assert list.search(42)
assert 1 == list.size()

list.insert(1, 12) # [42, 12]
assert 2 == list.size()
assert list.search(12)

print list.index(12)
