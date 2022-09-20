import numpy as np
import pandas as pd
import random

class hash_table():
    
    def random_hash_fn(self):
        self.p = 5915587277
        self.a = random.randint(1,self.p)
        self.b = random.randint(0,self.p)
    
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size
        self.random_hash_fn()

    def __str__(self):
        if self.size > 0:
            return str(self.data)
            
    def _hash(self, key):
        return ((self.a*key+self.b) % self.p) % self.size 
    
    def get(self, key):
        hash_ = self._hash(key)
        if self.data[hash_]:
            if len(self.data[hash_]) == 1:
                if self.data[hash_][0][0] == key:
                    return self.data[hash_][0][1]

            else:
                for i in range(len(self.data[hash_])):
                    if self.data[hash_][i][0] == key:
                        return self.data[hash_][i][1]
        return None    
    
    def set(self, key, value):
        hash_ = self._hash(key)
        if self.data[hash_]:
            self.data[hash_].append([key, value])
        else:
            self.data[hash_] = [[key, value]]
    
    def keys(self):
        keys = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j][0])
        if keys == []:
            return None
        return keys

    
a = hash_table(10)
a.data
a.set(1,10)
a.set(2,20)
a.set(3,30)
a.set(4,40)
a.get(1)
a.get(4)
a.keys()
    


        
def eval_collision_rate(size, load_fctr, sim_size=100):
    coll_lst = []
    for j in range(sim_size):
        a = hash_table(size)        
        for i in range(size*load_fctr):
            a.set(i,10*i)
            b = a.data
            coll_lst.append(np.mean([len(x) for x in b if x]))
    return coll_lst

coll_rate_dict = {}
for i in range(1,11):
    coll_rate_dict[i] = np.mean(eval_collision_rate(200,i))

coll_rate_df = pd.DataFrame.from_dict(coll_rate_dict.items())
coll_rate_df.columns = ['alpha','coll_rate']
coll_rate_df['coll_rate'].plot()