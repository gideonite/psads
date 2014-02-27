#!/usr/bin/python

def list_reverse(alist):
    if [] == alist:
        return []

    reversed_list = list_reverse(alist[1:])
    reversed_list.append(alist[0])

    return reversed_list

list_reverse([])
list_reverse([1])
list_reverse([1,2])
list_reverse([1,2,3])

def fibonacci(num_terms):
    if 0 == num_terms:
        return 0
    if 1 == num_terms:
        return 1

    return fibonacci(num_terms-1) + fibonacci(num_terms-2)

fibonacci(6)
fibonacci(5)
fibonacci(4)
fibonacci(3)
fibonacci(2)
fibonacci(1)
fibonacci(0)

def fib_gen():
    a,b = 0,1

    while 1:
        yield a
        a,b = b,a+b

# f = fib_gen()
# f.next()
# print [f.next() for i in range(100)]

def fibonacci2(num_terms):
    a,b = 0,1
    ret = []
    for i in range(num_terms+1):
        ret.append(a)
        a,b = b,a+b

    return ret[1:]     # don't want that first 0

fibonacci2(0)
fibonacci2(1)
fibonacci2(2)
fibonacci2(3)
fibonacci2(4)
fibonacci2(5)
fibonacci2(6)
fibonacci2(7)

def hanoi(num_disks):
    '''
    Iterative solution to the Tower of Hanoi problem.

    Sources:
        http://programmingpraxis.com/2011/10/11/tower-of-hanoi/
        http://www.ecse.rpi.edu/~wrf/p/28-sigplan84-hanoi.pdf
    '''
    towers = (range(num_disks), [], [])

    flip_patterns = ((0,1),(0,2),(1,2))

    last_moved = -1

    flip_index = 0
    while (num_disks != len(towers[2])+1):
        fm, to = flip_patterns[flip_index]

        print (fm, to), towers

        if not towers[fm] or (towers[to] and towers[to][-1] > towers[fm][-1]):
            to, fm = fm, to

        towers[to].append(towers[fm].pop())

        flip_index += 1
        flip_index %= 3

# hanoi(10)

import turtle

def hilbert(turtle, state, order, side_length):
    '''
    Lindenmayer System Rules (wikipedia.org/wiki/Hilbert_curve)
    Alphabet : A, B
    Constants : F + -
    Axiom : A
    Production rules:
        A -> - B F + A F A + F B -
        B -> + A F - B F B - F A +
    '''

    if order <= 0:
        return

    if 'A' == state:
        turtle.left(90)
        hilbert(turtle, 'B', order-1, side_length)
        turtle.forward(side_length)
        turtle.right(90)
        hilbert(turtle, 'A', order-1, side_length)
        turtle.forward(side_length)
        hilbert(turtle, 'A', order-1, side_length)
        turtle.right(90)
        turtle.forward(side_length)
        hilbert(turtle, 'B', order-1, side_length)
        turtle.left(90)
    elif 'B' == state:
        turtle.right(90)
        hilbert(turtle, 'A', order-1, side_length)
        turtle.forward(side_length)
        turtle.left(90)
        hilbert(turtle, 'B', order-1, side_length)
        turtle.forward(side_length)
        hilbert(turtle, 'B', order-1, side_length)
        turtle.left(90)
        turtle.forward(side_length)
        hilbert(turtle, 'A', order-1, side_length)
        turtle.right(90)
    else:
        return "FAIL"

def run_hilbert():
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()
    hilbert(turtle, 'A', 2, 60)
    myScreen.exitonclick()

def koch_side(turtle, order, side_length):
    if 0 == order:
        turtle.forward(side_length)
    else:
        koch(turtle, order-1, side_length/3)
        turtle.left(60)
        koch(turtle, order-1, side_length/3)
        turtle.right(60)
        turtle.right(60)
        koch(turtle, order-1, side_length/3)
        turtle.left(60)
        koch(turtle, order-1, side_length/3)

def run_snowflake():
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()

    koch_side(myTurtle, 2, 200)

    myScreen.exitonclick()

def problem14():
    items = [ {'weight': 2, 'value': 3},
              {'weight': 3, 'value': 4},
              {'weight': 4, 'value': 8},
              {'weight': 5, 'value': 8},
              {'weight': 9, 'value': 10} ]

    total_weight = 20
    weight_to_value = [0]
    for weight in range(1,total_weight+1):
        prev_value = weight_to_value[weight-1]
        choices = filter(lambda i: i['weight'] <= weight, items)

        if [] == choices:
            curr_value = prev_value
        else:
            curr_value = max(weight_to_value[weight-item['weight']] + item['value'] for item in choices)

        weight_to_value.append(curr_value)

    return max(weight_to_value)

def problem14(items, total_weight):
    '''
    You've got `total_weight` pounds of weight that you can carry.
    And you've got a list of items [{'weight', 'value'}]. You'd like
    to maximize the value that you pack into the bag.
    There are an infinite number of each item.
    '''
    weight_to_value = [0]
    for weight in range(1,total_weight+1):
        prev_value = weight_to_value[weight-1]
        choices = filter(lambda i: i['weight'] <= weight, items)

        if [] == choices:
            curr_value = prev_value
        else:
            curr_value = max(weight_to_value[weight-item['weight']] + item['value'] for item in choices)

        weight_to_value.append(curr_value)

    return max(weight_to_value)

items = [ {'weight': 2, 'value': 3},
          {'weight': 3, 'value': 4},
          {'weight': 4, 'value': 8},
          {'weight': 5, 'value': 8},
          {'weight': 9, 'value': 10} ]

problem14(items, 20)

def edit_distance_recursive(a, b):
    if not a:
        return len(b) * ins_cost
    if not b:
        return len(a) * ins_cost

    return min(edit_distance(a[1:], b[1:]) + (a[0] != b[0]) * sub_cost,
                edit_distance(a[1:], b) + sub_cost,
                edit_distance(a, b[1:]) + del_cost)

edit_distance_recursive("ab", "c")
