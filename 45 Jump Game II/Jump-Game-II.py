import unittest

class Solution:
    def jumpDP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10000 for i in range(n)]

        dp[0] = 0
        for i in range(n):
            for j in range(nums[i]):
                if i + j + 1 >= n:
                    break
                dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)

        return dp[n - 1]

    def jump(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        ci = 0
        mx = 0

        for i in range(n):
            mx = max(mx, i + nums[i])
            if ci == i and ci < n - 1:
                ci = mx
                ret += 1
                if ci >= n - 1:
                    break

        return ret
        
class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.jump([2,3,1,1,4]), 2)
    def test2(self):
        s = Solution()
        self.assertEqual(s.jump([2,3,0,1,4]), 2)
    def test3(self):
        s = Solution()
        self.assertEqual(s.jump([1,2,3]), 2)
    def test4(self):
        s = Solution()
        self.assertEqual(s.jump([1,1,1,1]), 3)
    def test5(self):
        s = Solution()
        self.assertEqual(s.jump([1]), 0)
    def test6(self):
        s = Solution()
        self.assertEqual(s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]), 2)

if __name__ == "__main__":
    unittest.main()