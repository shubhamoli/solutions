"""
    Leetcode #64
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for x in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

if __name__ == "__main__":

    solution = Solution()

    assert solution.minPathSum([[1,3,1], [1,5,1], [4,2,1]]) == 7
