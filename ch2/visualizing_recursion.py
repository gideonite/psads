#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle
import random

def drawSpiral(turtle, line_len):
    if line_len > 0:
        turtle.forward(line_len)
        turtle.right(90)
        drawSpiral(turtle, line_len-5)

def tree(branch_len, t):
    if branch_len > 5:

        t.pensize(branch_len/10)

        t.forward(branch_len)

        angle = random.randrange(15,46)
        random_offset = lambda : random.randrange(10,15)

        t.right(angle)
        tree(branch_len-random_offset(), t)
        t.left(2 * angle)
        tree(branch_len-random_offset(), t)
        t.right(angle)
        t.backward(branch_len)

def run_tree():
    t = turtle.Turtle()
    myScreen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myScreen.exitonclick()

# run_tree()
