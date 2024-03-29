class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.size = 0

        self.head = 0
        self.tail = -1
        self.max_size = k      


    def enQueue(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
                
        self.tail  = (self.tail + 1) % self.max_size
        self.arr[self.tail] = value
        
        self.size += 1
        
        # print(self.tail)
        
        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
