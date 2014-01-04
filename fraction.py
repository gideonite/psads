#!/usr/bin/python

from __future__ import division

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):
        if type(top) != int:
            raise TypeError("'" + str(top) + "'" + " is not an integer.")

        if type(bottom) != int:
            raise TypeError("'" + str(bottom) + "'" + " is not an integer.")

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def getNum():
        return self.num

    def getDen():
        return self.den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        minus_one = Fraction(-1,1)
        return self + (otherfraction*minus_one)

    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum, newden)

    def __div__(self, otherfraction):
        if otherfraction == Fraction(0,1):
            raise ZeroDivisionError
        else:
            return self * Fraction(otherfraction.den, otherfraction.num)

    def __truediv__(self, otherfraction):
        if otherfraction == Fraction(0,1):
            raise ZeroDivisionError
        else:
            return self * Fraction(otherfraction.den, otherfraction.num)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __cmp__(self, other):
        return (self.num * other.den) - (other.num * self.den)

x = Fraction(1,2)
y = Fraction(2,3)

#
# TESTS
#
zero = Fraction(0,1)
one = Fraction(1,1)

# multiply
assert x == x*one
assert Fraction(1,4) == x*x
assert Fraction(1,3) == y*x

# subtract
assert x == x-zero
assert Fraction(1,6) == y-x
assert Fraction(-1,6) == x-y

# divide
assert x == x / one
assert Fraction(4,3) == y / x
def divide_by_zero_test():
    try:
        x / zero
    except ZeroDivisionError:
        return True
assert divide_by_zero_test()

# less than and greater than
assert x > zero
assert not x < zero
assert x < y
assert not x > y

print "success!"
