#!/usr/bin/python

from queue import Queue

def radix_sort(items):

    main = Queue()

    # initialize
    for item in items:
        main.enqueue(item)

    index = 0

    num_chars = max(len(s) for s in items)
    for index in range(num_chars):
        bins = {}
        while 0 != main.size():
            item = main.dequeue()

            try:
                digit = item[index]
            except IndexError:
                digit = 0

            bins[digit] = bins.get(digit, Queue()).enqueue(item)

        digits = bins.keys()
        digits.sort(key=lambda(x): (x is None, x))

        for digit in digits:
            bin = bins[digit]
            while 0 != bin.size():
                item = bin.dequeue()
                main.enqueue(item)
        index+=1

    ret = []
    while 0 != main.size():
        ret.append(main.dequeue())

    return ret

assert ["1", "2", "3", "4"] == radix_sort(["1", "2", "3", "4"])
assert ["1", "2", "3", "4"] == radix_sort(["4", "2", "3", "1"])
#assert ["11", "2", "3", "4"] == radix_sort(["2", "3", "4", "11"])
#assert ["1", "11", "2", "3", "4"] == radix_sort(["11", "1", "2", "3", "4"])
#print radix_sort(["2", "3", "4", "11"])
#print radix_sort(["11", "1", "2", "3", "4"])
#print radix_sort(["11", "10", "1", "2", "3", "4"])
#print radix_sort(["01", "10", "11", "01", "02", "03", "04"])
