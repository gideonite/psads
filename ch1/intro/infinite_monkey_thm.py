#!/usr/bin/python

import random

goal = "methinks it is like a weasel"
goal_length = len(goal)

abcs = list("abcdefghijklmnopqrstuvwxyz ")
assert len(abcs) == 27

def random_word():
    return "".join([random.choice(abcs) for i in range(goal_length)])

def perturb(word):
    '''
    Leaves alone the letters that match the goal. Replaces the other with a
    random letter.
    '''
    ret = list(word)

    for i in range(goal_length):
        if word[i] != goal[i]:
            ret[i] = random.choice(abcs)

    return "".join(ret)


def score(w1, w2):
    word_length = len(w1)

    num_same = 0
    for i in range(word_length):
        if w1[i] == w2[i]:
            num_same+=1

    return float(num_same) / word_length

def search(seed, batch_size):
    score_num = 0

    for i in range(batch_size):
        seed = perturb(seed)
        score_num = score(seed, goal)

        if seed == goal:
            break

    print "%f\t%s" %(score_num, seed)

    return seed


def main():

    word = random_word()
    while 1:
        word = search(word, 1)
        if word == goal:
            break

if __name__ == "__main__":
    main()
