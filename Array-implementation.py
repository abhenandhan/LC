class array():
    
    def __init__(self):
        self.data = {}
        self.len = 0
        
    def __str__(self):
        return f'{self.data.values()}'
    
    def __len__(self):
        return self.len
    
    def get(self, index):
        if (index > self.len) | (index<0):
            print('Index too large or small')
            return 
        return self.data[index-1]
    
    def push(self, elem):
        self.data[self.len] = elem
        self.len += 1
    
    def pop(self):
        if self.len == 0:
            print('Empty list, nothing to pop')
        else:
            popped_elem = self.data[self.len-1]
            del self.data[self.len-1]
            self.len -= 1
            return popped_elem
    
    def insert(self, elem, index):
        if (index > self.len+1) | (index<=0):
            print('Index too large or small')
        elif index == self.len+1:
            self.push(elem)
        else:
            self.len += 1
            for i in range(index, self.len):
                self.data[i] = self.data[i-1]
            self.data[index-1] = elem
                
    def delete(self, index):
        if (index > self.len) | (index<0):
            print('Index too large or small')
            return
        elif index == self.len:
            self.pop()
        else:
            popped_elem = self.data[index-1]
            print(popped_elem)
            for i in range(index-1, self.len-1):
                self.data[i] = self.data[i+1]
            del self.data[self.len-1]
            self.len -= 1
        
                
            
            
        
a = array()
a.len
a.data.values()

a.pop()
a.push(10)

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

a.get(4)
a.get(1)
a.delete(2)
a.delete(4)

print(a)
len(a)
