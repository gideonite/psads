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

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    for op in prec.keys():
        infixexpr = infixexpr.replace(op, " " + op + " ")
    infixexpr = infixexpr.replace("(", " ( ")
    infixexpr = infixexpr.replace(")", " ) ")
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            if opStack.isEmpty():
                raise SyntaxError("')' has no matching parens")
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    if 1 == opStack.size() and 1 == len(postfixList):
        op = opStack.pop()
        raise SyntaxError("Operation " + "'" + op + "'" +  "must take more than one parameter. Given '" + postfixList[0] + "'.")

    while not opStack.isEmpty():
        op = opStack.pop()
        if "(" == op:
            raise SyntaxError("'(' has no matching parens")
        postfixList.append(op)

    return " ".join(postfixList)

# Possible errors
infixToPostfix("((A + B)")
infixToPostfix("(A + B))")
infixToPostfix("( A + ")
infixToPostfix("(A + ")
infixToPostfix("A + ")
infixToPostfix("+ B")
infixToPostfix("A + B + C * D")
infixToPostfix("A + B + C + D")

infixToPostfix("A+B")
infixToPostfix("A * B + C * D")
infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")
infixToPostfix("4 + 12 * ( A + B ) + C")