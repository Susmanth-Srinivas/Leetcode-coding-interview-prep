class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            ch = s[i - 1]
            # Traverse backwards so dp[j - 1] still holds the previous row's value
            upper = min(i, n)
            for j in range(upper, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]