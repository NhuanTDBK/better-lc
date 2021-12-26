from collections import defaultdict


class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.inc = []
        self.max_size = maxSize
        

    def push(self, x: int) -> None:
        if len(self.arr) == self.max_size:
            return
        
        self.arr.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if not self.arr:
            return -1
        
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        
        return self.arr.pop()  + self.inc.pop()
        

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k-1, len(self.arr)-1)] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
