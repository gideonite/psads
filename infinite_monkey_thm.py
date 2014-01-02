#!/usr/bin/python

import random

goal = "methinks it is like a weasel"

abcs = list("abcdefghijklmnopqrstuvwxyz ")
assert len(abcs) == 27

def random_word():
    goal_length = len(goal)
    return "".join([random.choice(abcs) for i in range(goal_length)])

def score(w1, w2):
    word_length = len(w1)

    score = 0
    for i in range(word_length):
        if w1[i] == w2[i]:
            score+=1

    return float(score) / word_length

def search(times):

    max = 0
    best = ''
    for i in range(times):
        word = random_word()
        s = score(word, goal)

        if s == 1:
            return word

        if s > max:
            max = s
            best = word
    print "%f\t%s" % (max, best)


def main():

    while 1:
        word = progress(1000)
        if word == goal:
            break

main()
