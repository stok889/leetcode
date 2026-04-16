class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                f = 1
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        f = 0
                        break
                if f == 1:
                    ret += 1

        return ret

if __name__ == "__main__":
    s = Solution()
    m = [[3,2,1],[1,7,6],[2,7,7]]
    print(s.equalPairs(m))
    m = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(s.equalPairs(m))    