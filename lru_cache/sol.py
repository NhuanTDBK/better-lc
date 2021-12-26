class Node():
    def __init__(self,key=None,value=None) -> None:
        self.key = key
        self.val = value
        self.next: Node = None 
        self.prev: Node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.max_capacity = capacity

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapper = {}
    
    def drop(self, node: Node,):
        prev_, next_ = node.prev, node.next
        
        prev_.next = next_ 
        next_.prev = prev_
        self.size -= 1


        del self.mapper[node.key]
        
    def add_to_head(self, node: Node, is_drop):
        if is_drop:
            self.drop(node)
        
        self.mapper[node.key] = node
        
        next_ = self.head.next
        
        node.next = next_
        node.prev = self.head

        self.head.next = node
        next_.prev = node

        self.size += 1

    def remove_tail(self,):
        node = self.tail.prev
        self.drop(node)


    def get(self, key: int) -> int:
        if key not in self.mapper:
            return -1

        node = self.mapper[key]

        self.add_to_head(node, True)

        return node.val

    def put(self, key: int, value: int) -> None:
        is_existed = False 

        if key in self.mapper:
            is_existed = True
            node = self.mapper[key]
            node.val = value
        else:
            node = Node(key, value)
        
        self.add_to_head(node, is_existed)

        if self.size > self.max_capacity:
            self.remove_tail()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
