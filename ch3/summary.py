import random

#
# BINARY SEARCH
#

def binary_search_helper(sorted_list, key, slice_start, slice_end):

    if slice_start == slice_end:
        return False

    midpoint = (slice_start + slice_end) // 2

    if key == sorted_list[midpoint]:
        return True
    elif key < sorted_list[midpoint]:
        # search the left part of the slice
        return binary_search_helper(sorted_list, key, slice_start, midpoint)
    else:
        # search the right part of the slice
        return binary_search_helper(sorted_list, key, midpoint+1, slice_end)

def binary_search(sorted_list, key):
    '''Exercise 3: Implement binary search without using the slice operator.'''
    return binary_search_helper(sorted_list, key, 0, len(sorted_list))

binary_search([1,2,3,4,5], 0)
binary_search([1,2,3,4,5], 1)
binary_search([1,2,3,4,5], 2)
binary_search([1,2,3,4,5], 3)
binary_search([1,2,3,4,5], 4)
binary_search([1,2,3,4,5], 5)

#
# HASH TABLES
#

class HashTable:
    '''
    Chaining implementation. Chaining resolves collisions by storing
    a collection items that hash to the same value at the
    corresponding location in the backing array.
    '''
    def ahash_f(self, astr):
        '''
        Dumbest thing possible. Sums all the integer values of the chars in astr.
        '''
        astr = repr(astr) # coerce into string
        return sum(ord(char) for char in astr)

    def __init__(self):
        self.array_size = 17
        self.count = 0
        self.load = 0
        self.load_threshold = .75
        self.array = [[] for i in range(self.array_size)]
        self.hash_f = self.ahash_f

    def resize(self):
        old_array = self.array
        self.array_size *= 2
        self.count = 0
        self.array = [[] for i in range(self.array_size)]

        for items in old_array:
            for k,v in items:
                self.put(k,v)

    def put(self, key, value):
        index = self.hash_f(key) % self.array_size

        written = False
        for i, (k,v) in enumerate(self.array[index]):
            if k == key:
                v = value
                self.array[index][i] = (key,value)
                written = True
        if not written:
            self.array[index].append((key,value))
            self.count+=1
            self.load = float(self.count) / self.array_size

            if self.load > self.load_threshold:
                self.resize()

    def get(self, key):
        index = self.hash_f(key) % self.array_size

        if self.array[index]:
            for k,v in self.array[index]:
                if k == key:
                    return v
        raise KeyError(key)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        index = self.hash_f(key) % self.array_size
        return [] != self.array[index]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put( key, value)

    def __delitem__(self, key):
        index = self.hash_f(key) % self.array_size

        # TODO, going through the list twice
        if key not in [k for (k,v) in self.array[index]]:
            raise KeyError(key)

        self.array[index] = [(k,v) for (k,v) in self.array[index] if k != key]
        return None

h = HashTable()
h.put("k1", 42)
h.get("k1")
h.put("k1", 12)
h.get("k1")
len(h)
"k1" in h
"abc" in h
42 in h
del h["k1"]
h.array
h.put("1", 1)
h.array
del h["1"]
try:
    del h["1"]
except KeyError:
    pass

class OpenAddrHashTable:
    '''
    Implementation of a hash table using "open addressing."
    Open addressing handles collisions by simply placing the
    collided (key,value) pair in the next available (not nil)
    location in the array. Lookup therefore is going to the
    hashed index location, checking whether the queried key
    and the key at that location match, and if not, linearly
    going through the list until it is found.
    '''

    def ahash_f(self, astr):
        '''
        Essentially computes the dot product between the integer values
        of the characters in `astr` and the vector [1,2,3,...].
        '''
        astr = str(astr)
        return sum(i+1 * ord(ch) for i, ch in enumerate(astr))

    def __init__(self):
        self.array_size = 17
        self.array = [None for i in range(self.array_size)]
        self.hash_f = self.ahash_f

    def indexify(self, key):
        return self.hash_f(key) % self.array_size

    def resize(self):
        self.array_size *= 2
        old_array = self.array
        self.array = [None for i in range(self.array_size)]

        for item in old_array:
            if item:
                (k,v) = item
                self.put(k,v)

    def put(self, key, value):
        start_index = self.indexify(key)
        curr_index = start_index

        while self.array[curr_index] and curr_index+1 != start_index:
            (k,v) = self.array[curr_index]

            # overwrite
            if k == key:
                self.array[curr_index] = (key,value)
                return

            curr_index = (curr_index+1) % self.array_size

        if curr_index+1 == start_index:
            # reached the end without finding a nil position
            self.resize()
            self.put(key, value)
        else:
            self.array[curr_index] = (key, value)

    def get(self, key):
        start_index = self.indexify(key)
        curr_index = start_index

        # loop around the array until we're back where we started
        while curr_index+1 != start_index:
            curr_index = (curr_index+1) % self.array_size
            item = self.array[curr_index]

            # item wasn't found in the contiguous list of non-None items
            if None == item:
                raise KeyError(key)

            (k,v) = item
            if k == key:
                return v

            raise KeyError(key)
    def delete(self, key):
        index = self.indexify(key)
        count = 0

        while self.array[index] and count != self.array_size:
            k,v = self.array[index]

            if k == key:
                self.array[index] = None
                return

            count+=1
            index = (index+1) % self.array_sizek

        raise KeyError(key)

h = OpenAddrHashTable()

h.put(12, 42)
h.put("a", 12)
h.put("b", 12)
h.put("b", 42)
h.array

myHash = OpenAddrHashTable()
for i in range(100):
    myHash.put(i, i)

myHash = OpenAddrHashTable()
myHash.put(1,1)
myHash.put(2,2)
myHash.put(3,3)
myHash.put(42,42)
myHash.put(42,12)
myHash.hash_f(12) % myHash.array_size
print myHash.array
myHash.hash_f(42) % myHash.array_size

myHash.array

myHash.delete(3)
try:
    myHash.delete(3)
except KeyError:
    pass
print myHash.array
