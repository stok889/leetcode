class Solution:
    def singleNumberLinearSpace(self, nums: List[int]) -> int:
        n = len(nums)
        m = 3 * 10**4 + 1
        ret = [0 for i in range(2 * m)]
        for i in range(n):
            p = nums[i] + m
            ret[p] = ret[p] + 1
        ans = 0
        for i in range(n):
            p = nums[i] + m
            if ret[p] == 1:
                ans = p - m
                break

        return ans

    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans ^= nums[i]

        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1]
    print(s.singleNumber(nums))
    nums = [4,1,2,1,2]
    print(s.singleNumber(nums))