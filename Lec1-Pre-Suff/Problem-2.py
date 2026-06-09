'''
Problem 2: Minimum Deletion Cost to Avoid Repeating Letters

Description: Given string s and array cost, return minimum cost to delete characters so no two adjacent are the same.

Example:

Input: s = "abaac", cost = [1, 2, 3, 4, 5]
Output: 3
Explanation: Delete 'a' at index 2 (cost=3)
'''



# def Sol(arr,cost):
#   minCost = 0
#   rightPointer = 1
#   minValue = 0
#   for x in range(len(arr)):
#     if rightPointer == len(arr):
#       return minCost
#     if arr[x] == arr[rightPointer]:
#       if cost[x] >= cost[rightPointer] and minValue == 0:
#         minCost += cost[rightPointer]
#         minValue = cost[rightPointer]
      
#       elif cost[rightPointer] < minValue:
#         minValue = cost[rightPointer]

#       else:
#         minCost += cost[x]
#     rightPointer +=1
    


def Sol(arr,cost):
  minCost = 0
  # rightPointer = 1
  maxValue = 0
  looped = False
  for x in range(len(arr) -1):
    if arr[x] == arr[x+1] and looped is  False:
      minCost += cost[x] + cost[x+1]
      maxValue = max(cost[x],cost[x+1])
      looped = True
    elif arr[x] == arr[x+1] and looped is True:
      minCost += cost[x+1]
      if cost[x+1] > maxValue:
        maxValue = cost[x+1]
    elif arr[x] != arr[x+1] and looped is True:
      minCost -= maxValue
      maxValue = 0
      looped = False
    
  if looped:
    minCost -= maxValue
  return minCost
    
  
# print(Sol("abaaac",[1,2,3,4,5,6]))