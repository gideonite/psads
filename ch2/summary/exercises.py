#!/usr/bin/python

def list_reverse(alist):
    if [] == alist:
        return []

    reversed_list = list_reverse(alist[1:])
    reversed_list.append(alist[0])

    return reversed_list

list_reverse([])
list_reverse([1])
list_reverse([1,2])
list_reverse([1,2,3])

def fibonacci(num_terms):
    if 0 == num_terms:
        return 0
    if 1 == num_terms:
        return 1

    return fibonacci(num_terms-1) + fibonacci(num_terms-2)

fibonacci(6)
fibonacci(5)
fibonacci(4)
fibonacci(3)
fibonacci(2)
fibonacci(1)
fibonacci(0)

def fib_gen():
    a,b = 0,1

    while 1:
        yield a
        a,b = b,a+b

f = fib_gen()
f.next()
print [f.next() for i in range(100)]

def fibonacci2(num_terms):
    a,b = 0,1
    ret = []
    for i in range(num_terms+1):
        ret.append(a)
        a,b = b,a+b

    return ret[1:]     # don't want that first 0

fibonacci2(0)
fibonacci2(1)
fibonacci2(2)
fibonacci2(3)
fibonacci2(4)
fibonacci2(5)
fibonacci2(6)
fibonacci2(7)

def hanoi(num_disks):
    '''
    Iterative solution to the Tower of Hanoi problem.

    Sources:
        http://programmingpraxis.com/2011/10/11/tower-of-hanoi/
        http://www.ecse.rpi.edu/~wrf/p/28-sigplan84-hanoi.pdf
    '''
    towers = (range(num_disks), [], [])

    flip_patterns = ((0,1),(0,2),(1,2))

    last_moved = -1

    flip_index = 0
    while (num_disks != len(towers[2])+1):
        fm, to = flip_patterns[flip_index]

        print (fm, to), towers

        if not towers[fm] or (towers[to] and towers[to][-1] > towers[fm][-1]):
            to, fm = fm, to

        towers[to].append(towers[fm].pop())

        flip_index += 1
        flip_index %= 3


hanoi(10)

# hanoi(range(4), [], [])
