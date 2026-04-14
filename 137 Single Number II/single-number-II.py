class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict()
        for i in range(n):
            p = nums[i]
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        ans = 0
        for x in list(d.keys()):
            if d[x] == 1:
                ans = x
                break

        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,3,2]
    print(s.singleNumber(nums))