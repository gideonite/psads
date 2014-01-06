#!/usr/bin/python

import copy

ex1 = [ [0,2,0,1],
        [4,0,0,2],
        [0,3,0,4],
        [1,0,0,3]   ]

ex2 = [ [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9] ]

def getBlock(i, j, puzzle,blocksize):
    '''
    Given a row i, column j, and sudoku puzzle, returns the block containing
    position i,j.
    '''

    ioffset = i%blocksize
    istart = i-ioffset
    iend = istart+blocksize

    joffset = j%blocksize
    jstart = j-joffset
    jend = jstart+blocksize

    puzzle = copy.deepcopy(puzzle)

    return [row[jstart:jend] for row in puzzle[istart:iend]]

assert getBlock(0,1,ex1,3) == getBlock(0,0,ex1,3)

def getColumn(j, puzzle):
    '''
    Returns the j-th column of the puzzle
    '''
    return [row[j] for row in puzzle]

def filled(l):
    return [item for item in l if (item != 0 and type(item) == int)]

assert [] == filled([0, {}])
assert [1,2] == filled([0,1,2])
assert [1,2,2] == filled([{},1,2,2])

def step(puzzle,numbers,blocksize):
    for i in range(len(puzzle)):
        row = puzzle[i]
        for j in range(len(row)):
            n = row[j]

            block = getBlock(i,j,ex2,blocksize)

            if type(n) == set and len(n) == 1:
                puzzle[i][j] = n.pop()
            elif 0 == n or set == type(n):
                constraints = filled(getColumn(j, puzzle) + \
                        #[i for row in getBlock(i,j,ex2) for i in row] + \
                        row)
                constraints = set(constraints)
                possibilities = numbers.difference(constraints)
                puzzle[i][j] = possibilities
    return puzzle
