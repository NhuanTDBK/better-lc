class MyStack:
    def __init__(self):
        self.fw = []
        self.bw = []

    def push(self, x: int) -> None:
        while len(self.fw) > 0:
            self.bw.append(self.fw.pop(0))
        
        self.fw.append(x)
        
        while len(self.bw) > 0:
            self.fw.append(self.bw.pop(0))
        
#         print(self.fw)
#         print(self.bw)
        
    def pop(self) -> int:
        return self.fw.pop(0)

    def top(self) -> int:
        return self.fw[0]

    def empty(self) -> bool:
        return len(self.fw) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
