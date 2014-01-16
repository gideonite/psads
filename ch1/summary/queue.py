#!/usr/bin/python

class Queue:
    '''
    A queue that supports, on average, constant time enqueue and dequeue.
    '''

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
        self.count = 0

    def isEmpty(self):
        return [] == self.enqueue_stack and [] == self.dequeue_stack

    def enqueue(self, item):
        self.count += 1
        self.enqueue_stack.append(item)

    def dequeue(self):
        self.count -= 1
        if [] == self.dequeue_stack:

            while [] != self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

            self.enqueue_stack = []

        return self.dequeue_stack.pop()

    def size(self):
        return self.count

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert 3 == q.size()
assert 1 == q.dequeue()
assert 2 == q.dequeue()
assert 3 == q.dequeue()
