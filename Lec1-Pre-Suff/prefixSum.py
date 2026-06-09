class solution():
  def __init__(self,arr):
    self.sum = [0]
    for x in range(len(arr)):
      self.sum.append(self.sum[-1]+arr[x])

    
  
  def sumRange(self,a,b):
    return self.sum[b+1] - self.sum[a]

x = solution([2, -1, 3, 5, -2, 4])

print(x.sumRange(0,2))