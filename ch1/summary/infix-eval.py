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

    for ch in reversed(expr_str.split(" ")):
        if ch in order.keys():
            if not operators.isEmpty() and order[operators.peek()] > order[ch]:
                op = operators.pop()
                n1 = numbers.pop()
                n2 = numbers.pop()

                result = doMath(op, n1, n2)
                numbers.push(result)
            operators.push(ch)
        else:
            n = int(ch)
            numbers.push(n)

    while not operators.isEmpty():
        op = operators.pop()
        n1 = numbers.pop()
        n2 = numbers.pop()

        result = doMath(op, n1, n2)
        numbers.push(result)

    return numbers.pop()

def doMath(op, n1, n2):
    result = None
    if "*" == op:
        result = n1 * n2
    if "/" == op:
        result = n1 / n2
    if "+" == op:
        result = n1 + n2
    if "-" == op:
        result = n1 - n2

    #print op, n1, n2, "=>", result

    return result

assert 12 == doMath("/", 48, 4)
assert -26 == infix_eval("2 * 3 - 48 / 4 - 4 * 5")
