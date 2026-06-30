
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
    self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.head = Node(None)
      self.tail = Node(None)
      self.head.next = self.tail
      self.tail.prev = self.head
      self.currentCap = 0
      self.cache = {}

    def get(self, key: int) -> int:
      value = self.cache.get(key)
      if value:
        ans = value.val
        self.currentCap -=1
      else:
        return -1
      value.next = self.head
      self.head = value
      return ans
      
    def put(self, key: int, value: int) -> None:
      N = Node(value)
      if self.currentCap < self.capacity:
        self.cache[key] = N
        N.next = self.head
        self.head = N
      else:
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)