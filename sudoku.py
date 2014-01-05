#!/usr/bin/python

ex = [  [5,3,0,0,7,0,0,0,0],\
        [6,0,0,1,9,5,0,0,0],\
        [0,9,8,0,0,0,0,6,0],\
        [8,0,0,0,6,0,0,0,3],\
        [4,0,0,8,0,3,0,0,1],\
        [7,0,0,0,2,0,0,0,6],\
        [0,6,0,0,0,0,2,8,0],\
        [0,0,0,4,1,9,0,0,5],\
        [0,0,0,0,8,0,0,7,9] ]

def getBlock(i, j, puzzle):
    '''
    Given a row i, column j, and sudoku puzzle, returns the block containing
    position i,j.
    '''
    ret = []
    for row in puzzle[0:3]:
        ret.append(row[0:3])
    return ret

#print getBlock('a','b', ex)

numbers = {1,2,3,4,5,6,7,8,9}

row = ex[0]
knowns = []
for el in row:
    if el != 0:
        knowns.append(el)
print knowns

for j in range(len(row)):
    if row[j] == 0:
        row[j] = numbers.symmetric_difference(knowns)

print row
