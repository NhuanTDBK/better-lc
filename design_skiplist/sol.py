max_level = 20
import random
from typing import List


class Node:
    def __init__(self, level, val):
        self.val = val 
        self.forward = [None] * level
        self.count = 1
        self.level = level

    def __repr__(self) -> str:
        return "Val = {}".format(self.val)

class Skiplist:
    def __init__(self, p = 0.5):
        self.p = p

        self.head = Node(max_level, float('-inf'))
        self.tail = Node(0, float("inf"))
        
        self.curr_level = 1

        for level in range(len(self.head.forward)):
            self.head.forward[level] = self.tail

    def search(self, target: int) -> bool:
        curr = self.head 

        for level in range(self.curr_level-1,-1,-1):
            while curr.forward[level].val < target:
                curr = curr.forward[level]
            
            if curr.forward[level].val == target:
                return True 
        
        return False

    def get_lower_bound(self, key) -> List[Node]:
        prev_nodes_in_cols = [None] * max_level

        curr = self.head

        for level in range(self.curr_level-1,-1,-1):
            while curr.forward[level].val < key:
                curr = curr.forward[level]
            
            prev_nodes_in_cols[level] = curr
        
        return prev_nodes_in_cols

    def get_level(self,):
        level = 1
        while random.random() < self.p and level < min(max_level, self.curr_level+1):
            level += 1            
        return level

    def add(self, num: int) -> None:
        prev_nodes_in_cols = self.get_lower_bound(num)
        
        curr: Node = prev_nodes_in_cols[0].forward[0]
        if curr.val == num:
            curr.count += 1
            return 
        
        node_level = self.get_level()
        # print("RAndom ", node_level)

        if node_level > self.curr_level:
            for level in range(self.curr_level, node_level):
                prev_nodes_in_cols[level] = self.head

            self.curr_level = node_level
        
        curr = Node(node_level, num)

        for level in range(node_level):
            curr.forward[level] = prev_nodes_in_cols[level].forward[level]
            prev_nodes_in_cols[level].forward[level] = curr
        
        return 

    def erase(self, num):
        prev_nodes_in_cols = self.get_lower_bound(num)

        # print(prev_nodes_in_cols)

        curr: Node = prev_nodes_in_cols[0].forward[0]

        if curr.val != num:
            return False
        
        if curr.count > 1:
            curr.count -= 1
            return True

        for level in range(self.curr_level):
            # Reach out of level
            if prev_nodes_in_cols[level].forward[level] != curr:
                break
            
            prev_nodes_in_cols[level].forward[level] = curr.forward[level]

        del curr

        # Recalculate height of 
        while self.curr_level > 1 and self.head.forward[self.curr_level-1] == self.tail:
            self.curr_level -= 1
        
        return True

skiplist = Skiplist()
skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
skiplist.add(1)
print(skiplist.search(0)) # return False
skiplist.add(4)
print(skiplist.search(1)) # return True
print(skiplist.erase(0))  # return False, 0 is not in skiplist.
print(skiplist.erase(1))  # return True
print(skiplist.search(1)) # return False, 1 has already been erased.
print(skiplist.erase(1))  # return True
print(skiplist.search(1)) # return False, 1 has already been erased.
