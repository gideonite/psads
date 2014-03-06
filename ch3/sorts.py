def bubble(alist):
    '''
    Bubble sort a list.
    Keep a short circuit flag. If it is not flipped in a pass,
    then the list is sorted and you are done.
    '''
    for end_index in range(len(alist)-1,0,-1):
        flipped = False
        for index in range(end_index):
            if alist[index+1] < alist[index]:
                flipped = True
                alist[index], alist[index+1] = alist[index+1], alist[index]
        if not flipped:
            return

alist = [42, 12, 5, 10, 100]
bubble(alist)
alist

alist = [54,26,93,17,77,31,44,55,20]
bubble(alist)
alist

def doubleBubble(alist):
    '''
    Like a bubble sort except that you alternate
    between bubbling up and bubbling down.

    a.k.a. Cocktail Sort.

    This algorithm helps with the "turtles and rabbits"
    problem with Bubble Sort. With Bubble Sort, large
    elements at the front of the list don't pose a problem.
    They effortlessly bubble to the end of the list (rabbits).
    Small items at the end of the list however, do take a long
    time to get to the front of the list (turtles). By alternating
    between bubbling up and bubbling down, you can avoid this problem.
    '''
    begin = 0
    end = len(alist)
    swapped = True

    while swapped:
        swapped = False

        # bubble up
        for index in range(begin, end-1):
            if alist[index+1] < alist[index]:
                swapped = True
                alist[index], alist[index+1] = alist[index+1], alist[index]

        # bubble down
        for index in range(end-1, -begin, -1):
            if alist[index] < alist[index-1]:
                swapped = True
                alist[index], alist[index-1] = alist[index-1], alist[index]

doubleBubble(alist)
alist

def selectionSort(alist):
    for end_stop in range(len(alist)-1,0,-1):
        maxPos = 0
        for loc in range(1,end_stop+1):
            if alist[loc] > alist[maxPos]:
                maxPos = loc
        alist[maxPos], alist[loc] = alist[loc], alist[maxPos]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
alist

# TODO shell sort