class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = 0
        n = len(nums)
        d = 1000000
        nums.sort()
        for i in range(0, n):
            for j in range(i + 1, n):
                c = nums[i] + nums[j]
                for k in range(j + 1, n):
                    s = c + nums[k]
                    t = abs(s - target) 
                    if t < d:
                        d = t
                        ret = s

        return ret
    
if __name__ == "__main__":
    s = Solution()
    n = [-1, 2, 1, -4]
    t = 1
    print(s.threeSumClosest(n, t))
    n = [0, 0, 0]
    t = 1
    print(s.threeSumClosest(n, t))
    n = [0,3,97,102,200]
    t = 300
    print(s.threeSumClosest(n, t))