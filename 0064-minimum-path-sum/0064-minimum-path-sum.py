class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # First row: only reachable from the left
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # First column: only reachable from above
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]