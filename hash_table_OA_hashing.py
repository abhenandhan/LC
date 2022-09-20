import numpy as np
import pandas as pd
import random
class hash_table_OA():
    
    def random_hash_fn(self):
        self.p = 5915587277
        self.a = random.randint(1,self.p)
        self.b = random.randint(0,self.p)
    
    def __init__(self, size, probe_seq='lin'):
        self.size = size
        self.probe_seq = probe_seq
        self.data = [None]*self.size
        self.random_hash_fn()

    def __str__(self):
        if self.size > 0:
            return str(self.data)
            
    def _hash(self, key):
        return ((self.a*key+self.b) % self.p) % self.size 

    def find_open_slot(self,seq):
        for slot in seq:
            if not(self.data[slot]):
                return slot
        return None
    
    def set(self, key, value):
        hash = self._hash(key)
        if self.probe_seq == 'lin':
            seq = [(hash+i) % self.size for i in range(self.size)]
        else:
            seq = [(hash+i**2) % self.size for i in range(self.size)]
        print(hash)
        print(seq)
        slot = self.find_open_slot(seq)
        if slot:
            self.data[slot] = [key, value]            
        else:
            print('Ran out of size!')
    
    def get(self, key):
        hash = self._hash(key)
        if self.probe_seq == 'lin':
            seq = [(hash+i) % self.size for i in range(self.size)]
        else:
            seq = [(hash+i**2) % self.size for i in range(self.size)]
        print(hash)
        print(seq)
        for slot in seq:
            if self.data[slot]:
                if self.data[slot][0] == key:
                    return self.data[slot][1]
            else:
                return None
    
    def keys(self):
        keys = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j][0])
        if keys == []:
            return None
        return keys
    
