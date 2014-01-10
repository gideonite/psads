#!/usr/bin/python

import timeit
import random

# EXERCISE 1
# list indexing list[i] is O(1)
def list_indexing_test():
    for list_len in range(10,10000,10):
        random_list = [random.randrange(10000) for i in range(list_len)]
        timer = timeit.Timer("random_list[random.randrange(list_len)]", "from __main__ import random, list_len, random_list")

        print timer.timeit(number=100)


# EXERCISE 2
# get/set item are O(1) for dicts
def dict_get_set_test():
    print "GET"
    for dict_len in range(10,10000,10):
        random_dict = {i : None for i in range(dict_len)}
        timer_get = timeit.Timer("random_dict[random.randrange(dict_len)]", "from __main__ import random, dict_len, random_dict")
        print timer_get.timeit(number=100)

    print "SET"
    for dict_len in range(10,10000,10):
        random_dict = {i : None for i in range(dict_len)}
        timer_set = timeit.Timer("random_dict[random.randrange(dict_len)] = 'OUCH'", "from __main__ import random, dict_len, random_dict")
        print timer_set.timeit(number=100)


# EXERCISE 3
# del on list versus del on dict
def del_list_vs_dict_test():
    list_time = 0
    dict_time = 0
    for coll_len in range(10,10000,1):
        random_list = [random.randrange(10000) for i in range(coll_len)]
        list_timer = timeit.Timer("del random_list[random.randrange(len(random_list))]", "from __main__ import random, random_list")
        list_time += list_timer.timeit(number=1)    # NB can't delete more items than there are in the list

        random_dict = {i : None for i in range(coll_len)}
        dict_timer = timeit.Timer("del random_dict[random.randrange(len(random_dict))]", "from __main__ import random, random_dict")
        dict_timer.timeit(number=1)

    print list_time
    print dict_time

# EXERCISE 4
# Find the kth smallest number in a list in O(n) time.
def kth_min(alist, k):
    '''
    Selects a pivot element randomly. Partitions the list into elements that
    are less than the pivot (lt) and elements that are greater than the pivot
    (gt).

    If there are k elements in lt, then the pivot element is precisely the k-th
    smallest and we have found the k-th smallest element in O(n) time.
    This happens with probability 1/n.

    If there are more than k elements in lt, then the k-th smallest is in lt.
    So recur on this list and we have O(log n).
    This happens with probability 1 - 1/k.

    If there are less than k elements in lt, then the k-th smallest is in gt.
    So recur on gt and k - len(lt).
    This happens with probability 1/k.
    '''

    pivot = random.choice(alist)

    gt, lt_eq = [], []
    for n in alist:
        if n <= pivot:
            lt_eq.append(n)
        else:
            gt.append(n)

    len_lt_eq = len(lt_eq)

    if len_lt_eq == k:
        return pivot

    if len_lt_eq < k:
        return kth_min(gt, k - len_lt_eq)

    if len_lt_eq > k:
        return kth_min(lt_eq, k)
