#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxOperationsNlogN(vector<int>& nums, int k) {
        int ret = 0;
        int n = nums.size();
        int u = 0;

        sort(nums.begin(), nums.end());

        while (n > 0 && u < n) {
            int x1 = u;
            int l = u + 1;
            int r = n;

            while (r - l > 1) {
                int m = (l + r) >> 1;
                if (nums[x1] + nums[m] > k) r = m;
                else l = m;
            }

            if (nums[x1] + nums[l] == k) {
                ++ret;
                nums.erase(nums.begin() + x1);
                nums.erase(nums.begin() + l - 1);
                n -= 2;
            } 
            else ++u;
        }

        return ret;        
    }

    int maxOperations(vector<int>& nums, int k) {
        int ret = 0;
        int n = nums.size();
        map<int, int> h;

        for (int i = 0; i < n; ++i) {
            if (h.find(nums[i]) == h.end()) h[nums[i]] = 1;
            else ++h[nums[i]];
        }

        for (int i = 0; i < n; ++i) {
            if (h[nums[i]] == 0) continue;
            --h[nums[i]];            
            if (h[k - nums[i]] == 0) continue;
            --h[k - nums[i]];
            ++ret;
        }

        return ret;        
    }
};

int main() {
    Solution s;
    vector<int> m({1, 2, 3, 4});
    printf("%d\n", s.maxOperations(m, 5));
    m = {3,1,3,4,3};
    printf("%d\n", s.maxOperations(m, 6));
}
