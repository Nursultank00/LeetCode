class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
    
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        
    def removeHelper(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insertHelper(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeHelper(self.cache[key])
            self.insertHelper(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeHelper(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insertHelper(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.removeHelper(lru)
            del self.cache[lru.key]