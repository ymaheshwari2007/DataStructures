class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num0 = 0
        left_pointer = 0
        right_pointer = 0
        max_len = 0
        for x in nums:
            if x == 0:
                num0 += 1
            while num0 > 1:
                if nums[left_pointer] == 0:
                    num0 -= 1
                left_pointer +=1
            right_pointer += 1
            if right_pointer - left_pointer > max_len:
                max_len = right_pointer - left_pointer
        return max_len - 1
            