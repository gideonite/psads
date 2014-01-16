#!/usr/bin/python

from queue import Queue

def hot_potato(name_list, num_range):

    q = Queue()

    for name in name_list:
        q.enqueue(name)

    while  q.size() > 1:
        for i in range(num_range):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()

print hot_potato(["a", "b", "c"], 3)
