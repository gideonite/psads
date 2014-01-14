#!/usr/bin/python

import sys

ex1 = [ [1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1]]

ex2 = [ [4,0,0,0,0,0,8,0,5],
        [0,3,0,0,0,0,0,0,0],
        [0,0,0,7,0,0,0,0,0],
        [0,2,0,0,0,0,0,6,0],
        [0,0,0,0,8,0,4,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,6,0,3,0,7,0],
        [5,0,0,2,0,0,0,0,0],
        [1,0,4,0,0,0,0,0,0]]

def next(i,j):

    size = 9    # N.B. all puzzles must have a square size.

    if size-1 == j:
        return (i+1,0)
    else:
        return (i, j+1)

def valid(P):
    '''
    For every row, column, and block, tests whether there are duplicates other
    than zero. If there are duplicates then return False, otherwise True.
    '''

    def getCol(P,j):
        col = []
        for row in P:
            col.append(row[j])
        return col

    def getBlock(P,i,j):
        '''
        Returns a 3x3 block as a list.
        '''

        i_corner = i-i%3
        j_corner = j-j%3

        block = []
        for i_block in range(3):
            for j_block in range(3):
                block.append(P[i_corner+i_block][j_corner+j_block])

        return block

    def has_dups(l):
        '''
        Returns True if there are duplicates in the list *other than zero*.
        '''
        for i in range(len(l)):
            if 0 != l[i] and l.index(l[i]) != i:
                return True
        return False

    for row in P:
        if has_dups(row):
            return False

    for j in range(len(P[0])):
        if has_dups(getCol(P,j)):
            return False

    for i in [0,3,6]:
        for j in [0,3,6]:
            if has_dups(getBlock(P,i,j)):
                return False

    return True

def some_zeros(P):
    for row in P:
        for n in row:
            if 0 == n:
                return True
    return False

def count_zeros(P):
    count = 0
    for row in P:
        for n in row:
            if 0 == n:
                count+=1
    return count

def solve(P, i_curr, j_curr):
    key = keyify(P)
    P2count[key] = P2count.get(key,0) + 1

    i_next, j_next = next(i_curr, j_curr)

    if 0 != P[i_curr][j_curr]:
        return solve(P, i_next, j_next)

    for n in range(1,10):
        P[i_curr][j_curr] = n
        if valid(P) and solve(P,i_next,j_next):
            return True

    P[i_curr][j_curr] = 0

    return False

#solve(ex2,0,0)
