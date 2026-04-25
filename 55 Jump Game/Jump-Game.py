class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ret = True
        n = len(nums)
        ci = 0

        for i in range(n):
            if i > ci:
                ret = False
                break
            ci = max(ci, i + nums[i])

        return ret
        
if __name__ == "__main__":
    s = Solution()
    f = s.canJump([2,3,1,1,4])
    if f:
        print("True")
    else:
        print("False")
    f = s.canJump([3,2,1,0,4])
    if f:
        print("True")
    else:
        print("False")        