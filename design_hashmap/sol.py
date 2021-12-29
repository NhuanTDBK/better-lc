default_size = 1000

from collections import namedtuple
from typing import List

Node = namedtuple("Node",["key","value"])

class MyHashMap:

    def __init__(self):
        self.arr: List[List[Node]] = [[] for _ in range(default_size)]


    def find_entry(self,key):
        return key % default_size

    def put(self, key: int, value: int) -> None:
        entry_idx = self.find_entry(key)

        for i in range(len(self.arr[entry_idx])):
            if self.arr[entry_idx][i].key == key:
                self.arr[entry_idx][i] = Node(key,value)
                return 
        
        self.arr[entry_idx].append(Node(key,value))

    def get(self, key: int) -> int:
        entry_idx = self.find_entry(key)

        for i in range(len(self.arr[entry_idx])):
            if self.arr[entry_idx][i].key == key:                
                return self.arr[entry_idx][i].value
        
        return -1

    def remove(self, key: int) -> None:
        entry_idx = self.find_entry(key)

        deleted_idx = -1

        for i in range(len(self.arr[entry_idx])):
            if self.arr[entry_idx][i].key == key:                
                deleted_idx = i
                break
        
        if deleted_idx != -1:
            self.arr[entry_idx].pop(deleted_idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
