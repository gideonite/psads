#!/usr/bin/python

def min1(l):
    min = l[0]
    for n in l:
        min = n
        for m in l:
            if n > m:
                min = m
                break
    return min

def min2(l):
    min = l[0]

    for n in l:
        if n < min:
            min = n

    return min
