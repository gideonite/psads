#!/usr/bin/python

#
# Tower of Hanoi
#

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        # move everything but the last disk to the intermediate pole
        moveTower(height-1, fromPole, withPole, toPole)
        # move the bottom-most disk to the destination pole
        moveDisk(fromPole, toPole)
        # move everything from the intermediate pole back to the destination pole
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print "moving disk from", fp, "to", tp

moveTower(3, "A", "B", "C")
