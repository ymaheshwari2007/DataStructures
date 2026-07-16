class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        total = sum(nums[:k])
        average = total/k
        for x in range(k, len(nums)):
            total += nums[x]
            total -= nums[left]
            left +=1
            if total/k > average:
                average = total/k
        return average