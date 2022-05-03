#Implementation of Chaining in Hash Tables using lists in python
class MyHash:
    def __init__(self, b):
        self.bucket = b
        self.table = [[] for x in range(b)]
    
    def insert(self, x):
        i = x % self.bucket
        self.table[i].append(x)
    
    def remove(self, x):
        i = x % self.bucket
        self.table[i].remove(x)
    
    def search(self, x):
        i = x % self.bucket
        return x in self.table[i]