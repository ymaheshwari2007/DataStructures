'''
Problem 2: Maximum Subarray Sum with Length K

Description: Find the maximum sum of any contiguous subarray of exactly k elements.

Example:

Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5, 1, 3] has maximum sum = 9

'''

from prefixSum import solution as PrefixSum
from suffixSum import SuffixSum


''' This problem I can see a sliding window solution to be used with prefix sum'''

class Prefix():
  def __init__(self,arr):
    self.sum = [0]
    for x in range(len(arr)):
      self.sum.append(self.sum[-1]+arr[x])
  
  def GetPrefix(self):
    return self.sum
    

def Sol(arr,k):
  maxSum = 0
  leftPointer = 0
  rightPointer = k
  maxLeft = 0
  
  P = Prefix(arr).GetPrefix()
  while rightPointer < len(arr):
    s = P[rightPointer] - P[leftPointer]
    if s > maxSum:
      maxSum = s
      maxLeft = leftPointer
    leftPointer +=1
    rightPointer +=1
  
  print(f"Subarray {arr[maxLeft:maxLeft+k]} has the max sum = {maxSum}")
  

Sol([2, 1, 5, 1, 3, 2],3)
  