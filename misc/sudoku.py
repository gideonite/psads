#!/usr/bin/python

ex1 = [ [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

def next(i,j):
    if i == 9 == j:
        return "Broke"

    if 9 == j:
        return (i+1,0)
    else:
        return (i, j+1)

def dups(l):
    '''
    Returns True if there are duplicates in the list.
    '''
    for i in range(len(l)):
        if l.index(l[i]) != i:
            return True
    return False

def getCol(P,j):
    col = []
    for row in P:
        col.append(row[j])
    return col

def getBlock(P,i,j):
    '''
    Returns a 3x3 block as a list.
    '''

    i_corner -= i%3
    j_corner -= j%3

    block = []
    for i_block in range(3):
        for j_block in range(3):
            block.append(P[i_corner+i_block][j_corner+j_block])

    return block

def valid(P):
    '''
    For every row, column, and block, tests whether there are duplicates other
    than zero. If there are duplicates then return False, otherwise True.
    '''

    for row in P:
        if dups(row):
            return False

    for j in range(len(P[0])):
        if dups(getCol(P,j)):
            return False

    for i in [0,3,6]:
        for j in [0,3,6]:
            if dups(getBlock(P,i,j)):
                return False

def has_zeros(P):
    for row in P:
        for n in row:
            if 0 == n:
                return True
    return False

def solve(P, i_curr, j_curr):

    i_next, j_next = next(i_curr, j_curr)

    if 0 != P[i_curr][j_curr]:
        solve(P, i_next, j_next)

    if not has_zeros(P) and valid(P):
        return P
    elif valid(P):
        for n in range(1,10):
            P[i_next, j_next] = n
            if valid(P):
                solve(P, i_next, j_next)

        P[i_next, j_next] = 0

        if 9 == P[i_curr][j_curr]:
            solve(P, i_prev_prev, j_prev_prev)
        else:
            P[i_curr][j_curr] += 1
            solve(P,i_curr,j_curr)
    else:
        return None

print solve(ex1,0,0)
