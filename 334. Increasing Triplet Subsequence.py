class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 103039049094949884848
        second = 103039049094949884848
        for x in nums:
            if x < first:
                first = x
            elif x < second:
                second = x
            else:
                return True
        return False