#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int ret = 0;
        int n = nums.size();
        int u = 0;

        sort(nums.begin(), nums.end());

        while (u < n) {
            int p = n - 1;
            int f = 0;
            
            /*
            while (u < p) {
                int s = nums[u] + nums[p];
                if (s > k) {
                    --p;
                    continue;
                }
                if (s == k) {
                    ++ret;
                    nums.erase(nums.begin() + u);
                    nums.erase(nums.begin() + p - 1);
                    f = 1;
                    n -= 2;
                    break;                    
                }
                if (s < k) break;
                --p;
            }
            */
            if (!f) ++u;
        }

        return ret;        
    }
};

int main() {
    Solution s;
    vector<int> m({1,2,3,4});
    printf("%d\n", s.maxOperations(m, 5));
    m = {3,1,3,4,3};
    printf("%d\n", s.maxOperations(m, 6));

    return 0;
}