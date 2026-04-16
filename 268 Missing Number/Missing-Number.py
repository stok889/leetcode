class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        nums.sort()
        for i in range(n):
            if nums[i] == ret:
                ret += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                break

        return ret