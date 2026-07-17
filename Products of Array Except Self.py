class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for x in range(0,len(nums)):
            prefix.append(prefix[x]*nums[x])
        suffix = [1 for x in range(len(nums)+1)]
        for x in range(len(nums)-1,-1,-1):
            suffix[x] = nums[x]*suffix[x+1]
        prefix = prefix[1:]
        suffix = suffix[:-1]
        ans = [suffix[1]]
        for x in range(1,len(nums)-1):
            ans.append(prefix[x-1]*suffix[x+1])
        ans.append(prefix[-2])
        return ans

