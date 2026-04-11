#include <bits/stdc++.h>

using namespace std;         

class Solution {
public:
    vector<int> twoSumO2(vector<int>& nums, int target) {
        vector<int> ret;
        int n = nums.size(), f = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] != target) continue;
                ret = {i, j};
                f = 1;
                break;
            }
            if (f) break;
        }

        return ret;
    }

    vector<int> twoSum2Pass(vector<int>& nums, int target) {
        map<int, int> h;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            h[nums[i]] = i;
        }

        for (int i = 0; i < n; ++i) {
            int x = target - nums[i];
            if (h.find(x) != h.end() && h[x] != i) {
                return {i, h[x]};
            }
        }

        return {};
    }

    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> h;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            int x = target - nums[i];
            if (h.find(x) != h.end() && h[x] != i) {
                return {i, h[x]};
            }
            h[nums[i]] = i;
        }

        return {};
    }
};

int main()
{
    Solution s;
    vector<int> a;
    vector<int> x({2, 7, 11, 15});

    a = s.twoSum(x, 9);
    printf("%d %d\n", a[0], a[1]);

    x = {3, 2, 4};
    a = s.twoSum(x, 6);
    printf("%d %d\n", a[0], a[1]);
    
	return 0;
}
