#!/usr/bin/python

ex = [  [5,3,{},{},7,{},{},{},{}],\
        [6,{},{},1,9,5,{},{},{}],\
        [{},9,8,{},{},{},{},6,{}],\
        [8,{},{},{},6,{},{},{},3],\
        [4,{},{},8,{},3,{},{},1],\
        [7,{},{},{},2,{},{},{},6],\
        [{},6,{},{},{},{},2,8,{}],\
        [{},{},{},4,1,9,{},{},5],\
        [{},{},{},{},8,{},{},7,9] ]

numbers = {1,2,3,4,5,6,7,8,9}

def getBlock(i, j, puzzle):
    '''
    Given a row i, column j, and sudoku puzzle, returns the block containing
    position i,j.
    '''

    ioffset = i%3
    istart = i-ioffset
    iend = istart+3

    joffset = j%3
    jstart = j-joffset
    jend = jstart+3

    return [row[jstart:jend] for row in puzzle[istart:iend]]

assert getBlock(0,1,ex) == getBlock(0,0,ex)

def getColumn(j, puzzle):
    '''
    Returns the j-th column of the puzzle
    '''
    return [row[j] for row in puzzle]

def filled(l):
    return [item for item in l if (item != 0 and type(item) == int)]

def flatten(l):
    return [j for i in l for j in i]

def run(puzzle):
    while 1:
        for i in range(len(puzzle)):
            row = puzzle[i]
        filled_in_row = filled(row)
        for j in range(len(row)):

            n = row[j]
            if type(n) == set and len(n) == 1:
                puzzle[i][j] = n.pop()

            if set == type(n):
                fs = filled(getColumn(j, puzzle)) +\
                        filled(flatten(getBlock(i,j,puzzle)) +\
                        filled_in_row)
                fs = set(fs)
                possibilities = numbers.difference(fs)
                puzzle[i][j] = possibilities

        print puzzle

        if [i for i in flatten(puzzle) if set == type(i)] == []:
            break

    print puzzle

run(ex)
