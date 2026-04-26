import unittest
from collections import deque

"""
assertEqual(a, b) a == b
assertNotEqual(a, b) a != b
assertTrue(x) bool(x) is True
assertFalse(x) bool(x) is False
assertIs(a, b) a is b
assertIsNot(a, b) a is not b
assertIsNone(x) x is None
assertIsNotNone(x) x is not None
assertIn(a, b) a in b
assertNotIn(a, b) a not in b
assertIsInstance(a, b) isinstance(a, b)
assertNotIsInstance(a, b) not isinstance(a, b)
assertIsSubclass(a, b) issubclass(a, b)
assertNotIsSubclass(a, b) not issubclass(a, b)
"""        

class Solution:
    def canReachListQueue(self, arr: List[int], start: int) -> bool:
        ret = False
        n = len(arr)
        f = [False for x in range(n)]
        q = []

        q.append(start)
        f[start] = True

        while len(q) > 0:
            u = q[0]
            q.pop(0)
            if arr[u] == 0:
                ret = True
                break
            if u - arr[u] >= 0 and not f[u - arr[u]]:
                f[u - arr[u]] = True
                q.append(u - arr[u])

            if u + arr[u] < n and not f[u + arr[u]]:
                f[u + arr[u]] = True
                q.append(u + arr[u])

        return ret

    def canReach(self, arr: List[int], start: int) -> bool:
        ret = False
        n = len(arr)
        f = [False for x in range(n)]
        q = deque()

        q.append(start)
        f[start] = True

        while len(q) > 0:
            u = q[0]
            q.popleft()
            if arr[u] == 0:
                ret = True
                break
            if u - arr[u] >= 0 and not f[u - arr[u]]:
                f[u - arr[u]] = True
                q.append(u - arr[u])

            if u + arr[u] < n and not f[u + arr[u]]:
                f[u + arr[u]] = True
                q.append(u + arr[u])

        return ret
        
class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        try:
            self.assertTrue(s.canReach([4,2,3,0,3,1,2], 5))
        except Exception:
            print("Error")

    def test2(self):
        s = Solution()
        try:
            self.assertTrue(s.canReach([4,2,3,0,3,1,2], 0))
        except Exception:
            print("Error")

    def test3(self):
        s = Solution()
        try:
            self.assertTrue(s.canReach([3,0,2,1,2], 2))
        except Exception:
            print("Error")

if __name__ == "__main__":    
    unittest.main()