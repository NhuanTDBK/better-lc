class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
            
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        
        self.size += 1
        
        node = Node(val)

        if index == 0:
            node.next = self.head
            self.head = node
            return 

        curr = self.head
        for _ in range(index-1):
            curr = curr.next    

        node.next = curr.next 
        curr.next = node


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        
        self.size -= 1

        # remove to head
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head 
        for _ in range(index-1):
            curr = curr.next
        
        curr.next = curr.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
