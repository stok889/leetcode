class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = 0
        n = len(candies)
        ret = [False for i in range(n)]        

        for i in range(n):
            if m < candies[i]:
                m = candies[i]

        for i in range(n):
            if m <= candies[i] + extraCandies:
                ret[i] = True

        return ret

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,5,1,3]
    print(s.kidsWithCandies(nums, 3))
    nums = [4,2,1,1,2]
    print(s.kidsWithCandies(nums, 1))