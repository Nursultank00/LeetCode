from random import randint

class RandomizedSet:

    def __init__(self):
        self.positions = {}
        self.rset = []

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        else:
            self.positions[val] = len(self.rset)
            self.rset.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        else:
            position = self.positions.pop(val)
            replace = self.rset.pop()
            
            if replace != val:
                self.rset[position] = replace
                self.positions[replace] = position
            
            return True 
        
    def getRandom(self) -> int:
        n = len(self.rset) - 1
        number = randint(0, n)
        return self.rset[number]