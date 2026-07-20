class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap.keys():
                hashmap[i] = [1,k-i]
            else:
                hashmap[i][0] +=1

        count = 0    
        for i in hashmap.keys():
            difference = k - i
            if difference in hashmap.keys():
                count += min(hashmap[i][0], hashmap[difference][0])
        return count//2
  