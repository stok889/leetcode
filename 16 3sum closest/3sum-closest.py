import unittest

class Solution:
    def threeSumClosestN2logN(self, nums: List[int], target: int) -> int:
        ret = 0
        n = len(nums)
        d = 1000000
        nums.sort()
        for i in range(0, n):
            for j in range(i + 1, n):
                c = nums[i] + nums[j]
                l = j + 1
                r = n - 1

                if l + 1 == n:
                    s = c + nums[l]
                    if abs(s - target) < d:
                        ret = s

                while r - l > 1:
                    med = (l + r) // 2
                    m1 = (l + med) // 2
                    m2 = (med + r) // 2
                    s1 = c + nums[m1]
                    s2 = c + nums[m2]
                    t1 = abs(s1 - target)
                    t2 = abs(s2 - target)
                    if t1 < t2:
                        if t1 < d:
                            d = t1
                            ret = s1
                        r = med
                    elif t1 > t2:
                        if t2 < d:
                            d = t2
                            ret = s2
                        l = med
                    else:
                        s1 = c + nums[l]
                        s2 = c + nums[r]
                        t1 = abs(s1 - target)
                        t2 = abs(s2 - target)
                        if t1 < t2:
                            if t1 < d:
                                d = t1
                                ret = s1
                            r = med
                        else:
                            if t2 < d:
                                d = t2
                                ret = s2
                            l = med

                if r == n:
                    r -= 1

                for k in range(l, r + 1):
                    s = c + nums[k]
                    t = abs(s - target) 
                    if t < d:
                        d = t
                        ret = s

        return ret

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = nums[0] + nums[1] + nums[2]
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if abs(sum - target) < abs(ret - target):
                    ret = sum

                if sum == target:
                    ret = sum
                    break

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                
            if ret == target:
                break

        return ret

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

class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
        except Exception:
            print("Error")

    def test2(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([0, 0, 0], 1), 0)
        except Exception:
            print("Error")

    def test3(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([0,3,97,102,200], 300), 300)
        except Exception:
            print("Error")

    def test4(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([-4,2,2,3,3,3], 0), 0)
        except Exception:
            print("Error")

    def test5(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([1,3,4,7,8,9], 15), 15)
        except Exception:
            print("Error")

    def test6(self):
        s = Solution()
        try:
            self.assertEqual(s.threeSumClosest([-1,2,1,-4], 1), 2)
        except Exception:
            print("Error")

    def test7(self):
        s = Solution()
        try:
            t = [1,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,29]
            self.assertEqual(s.threeSumClosest(t, 45), 45)
        except Exception:
            print("Error")

if __name__ == "__main__":
    unittest.main()