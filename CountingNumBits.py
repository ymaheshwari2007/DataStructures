class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n==2:
            return [0,1,1]
        dp = [0,1,1]
        highest = 2
        for i in range(3,n+1):
            if i == highest*2:
                highest = highest*2
            dp.append(dp[i-(highest)] + 1)
        return dp
