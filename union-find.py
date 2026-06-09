class basic_union_find:
  def __init__(self,n:int):
    self.array = [x for x in range(n)]
  
  def find(self,n):
    while n != self.array[n]:
      n = self.array[n]
    return n
  
  def union(self,a,b):
    parent_a = self.find(a)
    self.array[self.find(b)]= parent_a
  
    
class rank_union_find:
  def __init__(self,n:int):
    self.array = [x for x in range(n)]
    self.rank = [0 for x in range(n)]
  
  def find(self,n):
    # self.rank[n] = 0
    distance = 0
    index = n
    while n != self.array[n]:
      n = self.array[n]
      distance +=1
    
    if self.rank[self.find(index)] < distance:
      self.rank[self.find(index)] = distance
    return n
  
  def union(self,a,b):
    parent_a = self.find(a)
    self.array[self.find(b)]= parent_a
  
  def rank_union(self,a,b):
    if self.rank[self.find(a)] >= self.rank[self.find(b)]:
      self.union(a,b)
    else:
      self.union(b,a)