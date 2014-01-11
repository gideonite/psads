#!/usr/bin/python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def infixEval(expr):
    if "" == expr:
        return expr

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    operators = Stack()
    operands = Stack()

    tokens = expr.split()
    for token in tokens:
        if token in "0123456789":
            operands.push(int(token))

            while (not operators.isEmpty()):
                op = operators.pop()
                arg2 = operands.pop()
                arg1 = operands.pop()
                result = doMath(op, arg1, arg2)
                operands.push(result)

def doMath(op, arg1, arg2):
    '''
    string, int, int -> int.
    Assumes that the operator is one of "+", "-", "*", "/".
    '''
    if "*" == op:
        return arg1 * arg2

    if "/" == op:
        return arg1 / arg2

    if "+" == op:
        return arg1 + arg2

    if "-" == op:
        return arg1 - arg2

doMath("+", 1, 2)

infixEval("")
infixEval("1 + 2")
infixEval("1 * 1")
infixEval("1 + 1 + 1")
#infixEval("5 * 20 + 10")