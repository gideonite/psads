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

def infix_eval(expr_str):
    operators = Stack()
    numbers = Stack()

    order = {}
    order["*"] = 2
    order["/"] = 2
    order["+"] = 1
    order["-"] = 1

    for ch in expr_str.split(" "):
        if ch in order.keys():
            operators.push(ch)
        else:   # number
            n = int(ch)
            numbers.push(n)
            if not operators.isEmpty():
                n2 = numbers.pop()
                n1 = numbers.pop()
                op = operators.pop()

                result = doMath(op, n1, n2)
                numbers.push(result)

    while not operators.isEmpty():
        op = operators.pop()
        n2 = numbers.pop()
        n1 = numbers.pop()

        result = doMath(op, n1, n2)
        numbers.push(result)

    return numbers.pop()

def doMath(op, n1, n2):
    if "*" == op:
        return n1 * n2
    if "/" == op:
        return n1 / n2
    if "-" == op:
        return n1 - n2
    if "+" == op:
        return n1 + n2

print infix_eval("2 * 3 - 48 / 4 - 4 * 5")
