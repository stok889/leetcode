class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ret = 1
        n = len(nums)

        nums.sort()
        for i in range(n):
            if nums[i] <= 0:
                continue
            if nums[i] == ret:
                ret += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                break

        return ret

if __name__ == "__main__":
    s = Solution()
    m = [1,2,0]
    print(s.firstMissingPositive(m))
    m = [3,4,-1,1]
    print(s.firstMissingPositive(m))    
    m = [7,8,9,11,12]
    print(s.firstMissingPositive(m))        
    m = [0,2,2,1,1]
    print(s.firstMissingPositive(m))        
    m = [1]
    print(s.firstMissingPositive(m))            
    m = [1, 1]
    print(s.firstMissingPositive(m))                
    m =  [9,6,4,2,3,5,7,0,1]
    print(s.firstMissingPositive(m))                