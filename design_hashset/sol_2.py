from collections import namedtuple
from typing import List

Node = namedtuple("Node",["key"])

EMPTY_NODE = Node(-1)
DELETED_NODE = Node(-1)

class MyHashSet:

    def __init__(self):
        self.arr: List[Node] = [EMPTY_NODE] * 1000
        self.load_factor = 0.75
        self.size = 0
        self.deleted_size = 0

    def resize(self):
        self.old_arr = self.arr[:]

        self.arr = [EMPTY_NODE] * (len(self.arr) * 3)
        
        self.size = 0
        self.deleted_size = 0

        for i in range(len(self.old_arr)):
            if self.old_arr[i] != EMPTY_NODE or self.old_arr[i] != DELETED_NODE:
                self.add(self.old_arr[i].key)

        return

    def add(self, key: int) -> None:
        root_idx = hash(key) 

        for offset in range(len(self.arr)):
            current_idx = (root_idx + offset) % len(self.arr)

            current_node = self.arr[current_idx]

            if current_node.key == key or current_node == EMPTY_NODE or current_node == DELETED_NODE:
                self.arr[current_idx] = Node(key)
                self.size += 1
                break
        
        if (self.size + self.deleted_size) / self.load_factor > len(self.arr):
            self.resize()


    def remove(self, key: int) -> None:
        root_idx = hash(key) 

        for offset in range(len(self.arr)):
            current_idx = (root_idx + offset) % len(self.arr)

            current_node = self.arr[current_idx]

            if current_node.key == key:
                self.arr[current_idx] = DELETED_NODE
                self.size -= 1
                self.deleted_size += 1

                return

        return 

    def contains(self, key: int) -> bool:
        root_idx = hash(key) 

        for offset in range(len(self.arr)):
            current_idx = (root_idx + offset) % len(self.arr)

            current_node = self.arr[current_idx]

            if current_node.key == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
