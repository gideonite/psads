#!/usr/bin/python

class HashTable:
    self.hash_f
    self.array    # an array of lists
    self.count = 0
    self.load_balance

    def __init__(self, size=8):
        self.array = range(size)
    def put(self, key, value):
        index = self.hash_f(k) % len(self.array)

        # Copy the list of values associated with the hashed key,
        # replacing the value associated with this particular key with the new value.
        value_list = []
        updated = False
        for (k, v) in self.array.get(index, []):
            if key == k:
                value_list.append((key, value))
                updated = True
            else:
                value_list.append((k,v))
        if not updated:
            value_list.append((key, value))
        self.array[index] = value_list

    def get(self, k):
        index = self.hash_f(k) % len(self.array)
        for (key, v) in self.array[index]:
            if key == k:
                return v
        return None

max(initial_size, # of puts)

# self.array[index] = self.array.get(index, []).append((key, v))

