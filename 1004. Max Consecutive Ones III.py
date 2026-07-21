class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num0 = 0
        l_pointer = 0
        r_pointer = 0
        max_len = 0
        for x in range(len(nums)):
            if nums[x] == 0:
                num0 += 1
            
            while num0 > k:
                if nums[l_pointer] == 0:
                    num0 -=1
                l_pointer += 1
            r_pointer +=1
            if r_pointer - l_pointer > max_len:
                max_len = r_pointer - l_pointer
            
        return max_len 
