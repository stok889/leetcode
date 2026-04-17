class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = [0, 0]
        n = len(nums)
        x = 0

        for i in range(n):
            x ^= nums[i]
            
        #x = xor(a, b)
        #x & 2^n, n - right position, where x & 2^n == 1
        #for i = 1, n
        # nums[i] & 2^n == 0, res[0] ^= nums[i]
        #res[1] = x ^ res[0]

        b = 0
        for i in range(32):
            if (x & (1 << i)):
                b = i
                break
        
        for i in range(n):
            if not(nums[i] & (1 << b)):
                ret[0] ^= nums[i]

        ret[1] = ret[0] ^ x

        return ret
        
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1,3,2,5]
    print(s.singleNumber(nums))