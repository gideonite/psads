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

def draw_triangle(points, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()

    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()

def midpoint(p,q):
    return ( (p[0]+q[0]) / 2, (p[1]+q[1]) / 2)

def siepinksi(points, degree, turtle):
    colors = ['blue','red','green','white','yellow','violet','orange']

    draw_triangle(points, colors[degree], turtle)

    if degree > 0:
        siepinksi([points[0],\
                    midpoint(points[0], points[1]),\
                    midpoint(points[0], points[2])],\
                degree-1, turtle)
        siepinksi([points[1],\
                    midpoint(points[0], points[1]),\
                    midpoint(points[1], points[2])],\
                degree-1, turtle)
        siepinksi([points[2],\
                    midpoint(points[2], points[1]),\
                    midpoint(points[0], points[2])],\
                degree-1, turtle)

def run_siepinski():
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()
    points = [[-100,-50], [0,100], [100,-50]]
    siepinksi(points, 3, myTurtle)
    myScreen.exitonclick()

run_siepinski()
