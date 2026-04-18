class Solution:
    def removeStars(self, s: str) -> str:
        ret = ""
        n = len(s)
        n1 = 0

        for i in range(n):
            if s[i] != '*':
                ret += s[i]
                n1 += 1
            elif s[i] == '*':
                ret = ret[:n1 - 1]
                n1 -= 1

        return ret        

if __name__ == "__main__":
    s = Solution()
    print(s.removeStars("leet**cod*e"))
    print(s.removeStars("erase*****"))