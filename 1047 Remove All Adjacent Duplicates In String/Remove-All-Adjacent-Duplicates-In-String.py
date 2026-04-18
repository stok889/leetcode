class Solution:
    def removeDuplicatesPointerSimulation(self, s: str) -> str:
        ret = s
        p = 0

        while p < len(ret):
            if p == 0:
                p += 1
                continue
            if ret[p] == ret[p - 1]:
                ret = ret[:p - 1] + ret[p + 1:]
                p -= 1
            else:
                p += 1

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("abbaza"))
    print(s.removeDuplicates("azxxzy"))
    print(s.removeDuplicates("aaaaaaa"))
    print(s.removeDuplicates("aaaaaaa"))
    