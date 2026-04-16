class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            grid[i].sort()

        for i in range(m):
            cm = 0
            for j in range(n):
                if cm < grid[j][m - i - 1]:
                    cm = grid[j][m - i - 1]
            ret += cm

        return ret
        
if __name__ == "__main__":
    s = Solution()
    m = [[1,2,4],[3,3,1]]
    print(s.deleteGreatestValue(m))
    m = [[10]]
    print(s.deleteGreatestValue(m))