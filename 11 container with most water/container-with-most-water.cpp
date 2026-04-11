#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int ret = 0;
        int n = height.size();
        int p1 = 0, p2 = n - 1;

        while (p1 < p2) {
            int ca = min(height[p1], height[p2]) * (p2 - p1);
            if (ret < ca) ret = ca;

            if (height[p1] > height[p2]) --p2;
            else ++p1;
        }

        return ret;
    }
};

int main() {
    Solution s;
    vector<int> m({1,8,6,2,5,4,8,3,7});
    printf("%d\n", s.maxArea(m));

    m = {1,1};
    printf("%d\n", s.maxArea(m));

    return 0;
}
