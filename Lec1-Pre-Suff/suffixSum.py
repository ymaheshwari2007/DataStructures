class SuffixSum:
  def __init__(self,arr):
    self.suffix = [sum(arr)]
    for x in range(len(arr)):
      self.suffix.append(self.suffix[-1]-arr[x])
  
  def getSuffix(self):
    return self.suffix


x = SuffixSum([2, 3, 1, 4, 5])

print(x.getSuffix())