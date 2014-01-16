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

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            except IndexError:
                raise SyntaxError("Only one operand provided to '" + token + "'.")
            result = doMath(token,operand1,operand2)
            operandStack.push(result)

    if operandStack.size() != 1:
        raise SyntaxError("More than two operands provided to '" + token + "'")
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# postfixEval('+ 1')
# postfixEval('1 + ')
# postfixEval('1 1 1 +')
# postfixEval('7 8 + 3 2 + /')
