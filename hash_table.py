"""
in this file a hash table becomes implemented. after the inital table is created
I will figure out a way to implement it
"""

initial = 20 # size of my table

class Node:
    def __init__(self,key, value): # basic Node template
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value,
                                               self.next != None)
    def __repr__(self):
        return str(self)


# Hash table object
class HashTable:
    def __init__(self):
        self.capacity = initial
        self.size = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        hashsum = 0
        # for each character in the key
        for x, c in enumerate(key):
            hashsum += (x + len(key))**ord(c)
            hashsum = hashsum % self.capacity

        return hashsum


# insert a value
    def insert(self,key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        # check if bucket is empty
        if node is None:
            # create node, add it, return
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        # add a node
        prev.next = Node(key, value)


    def find(self,key):
        index = self.hash(key)

        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value


    def remove(self,key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            self.size -= 1
            temp = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return temp