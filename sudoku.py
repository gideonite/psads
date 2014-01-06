#!/usr/bin/python

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

    return [row[jstart:jend] for row in puzzle[istart:iend]]

assert getBlock(0,1,ex1,3) == getBlock(0,0,ex1,3)

def getColumn(j, puzzle):
    '''
    Returns the j-th column of the puzzle
    '''
    return [row[j] for row in puzzle]

def filled(l):
    '''
    Filters the list `l` for values that are already filled in.
    That is, nonzero integers (and not sets which represent possible values for
    a element).
    '''
    return [item for item in l if (item != 0 and type(item) == int)]

assert [] == filled([0, {}])
assert [1,2] == filled([0,1,2])
assert [1,2,2] == filled([{},1,2,2])

def step(puzzle,numbers,blocksize):
    for i in range(len(puzzle)):
        row = puzzle[i]
        for j in range(len(row)):
            n = row[j]

            if type(n) == set and len(n) == 1:
                puzzle[i][j] = n.pop()
            elif 0 == n or set == type(n):
                block = getBlock(i,j,ex2,blocksize)

                constraints = filled(getColumn(j, puzzle) + \
                                        [block_i for block_j in block for block_i in block_j] + \
                                        row)
                constraints = set(constraints)
                possibilities = numbers.difference(constraints)
                puzzle[i][j] = possibilities
    return puzzle

def solve_9x9(puzzle):
    numbers = {1,2,3,4,5,6,7,8,9}

    for i in range(15):
        puzzle = step(puzzle, numbers, 3)

    return puzzle

print solve_9x9(ex2)
