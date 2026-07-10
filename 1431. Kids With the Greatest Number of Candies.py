class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m_candies = max(candies)
        out = []
        for candy in candies:
            if candy + extraCandies >= m_candies:
                out.append(True)
            else:
                out.append(False)
        
        return out
  