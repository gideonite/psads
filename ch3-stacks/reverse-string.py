#!/usr/bin/python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def testEqual(a,b):
    if a == b:
        pass
    else:
        raise Exception("Test failed! '" + a + "' does not equal '" + b + "'")

def revstring(mystr):
    stack = Stack()
    for ch in mystr:
        stack.push(ch)

    ret = []
    while not stack.isEmpty():
        ret.append(stack.pop())

    return "".join(ret)

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
