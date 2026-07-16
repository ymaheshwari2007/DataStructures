class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -10000
        left = 0
        right = len(heights) -1

        while right > left:
            print(left)
            print(right)
            volume = (right-left)*min(heights[left],heights[right])
            if volume > ans:
                ans = volume
            
            if heights[left] >= heights[right]:
                right -=1
            else:
                left +=1
        return ans