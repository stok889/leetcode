class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = []

        for i in range(n):
            cm = []
            for j in range(m):
                cm.append(1000000)
            ans.append(cm)

        ans[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    ans[i][j] = ans[i][j - 1] + grid[i][j]
                if i != 0 and j == 0:
                    ans[i][j] = ans[i - 1][j] + grid[i][j]
                else:
                    ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + grid[i][j]

        return ans[n - 1][m - 1]

if __name__ == "__main__":
    s = Solution()
    m = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minPathSum(m))
    m = [[1,2,3],[4,5,6]]
    print(s.minPathSum(m))