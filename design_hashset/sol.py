default_size = 1000

class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(default_size)]

    def get_entry(self, key):
        return key % default_size
        
    def add(self, key: int) -> None:
        entry_idx = self.get_entry(key)
        
        if key not in self.arr[entry_idx]:
            self.arr[entry_idx].append(key)            
        
    def remove(self, key: int) -> None:
        entry_idx = self.get_entry(key)
        
        if key not in self.arr[entry_idx]:
            return
        
        self.arr[entry_idx].remove(key)

    def contains(self, key: int) -> bool:
        entry_idx = self.get_entry(key)
        
        return key in self.arr[entry_idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
