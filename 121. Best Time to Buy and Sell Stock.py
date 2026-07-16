class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        low = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                this = prices[i] - low
                if this > high:
                    high = this
        return high
      
      