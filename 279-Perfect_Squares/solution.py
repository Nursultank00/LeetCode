# Снизу вверх dp, либо можно использовать BFS

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n+1)
        dp[0] = 0
        ps = []
        count = 1
        while count*count <= n:
            ps.append(count*count)
            count += 1
        for i in range(n):
            for item in ps:
                if i+item < len(dp):
                    dp[i+item] = min(dp[i] + 1,dp[i+item])
        return dp[n]