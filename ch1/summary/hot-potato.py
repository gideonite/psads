#!/usr/bin/python

import random
from queue import Queue

def hot_potato(name_list, round_len):

    q = Queue()

    for name in name_list:
        q.enqueue(name)

    while  q.size() > 1:
        round = random.randint(0, round_len)
        print round
        for i in range(round):
            q.enqueue(q.dequeue())

        if 0 != round:
            q.dequeue()

    return q.dequeue()

print hot_potato(["a", "b", "c"], 1)
