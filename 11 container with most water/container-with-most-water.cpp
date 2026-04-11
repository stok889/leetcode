#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int ret = 0;
        int n = height.size();
        //vector<pair<int, int> > m;

        //for (int i = 0; i < n; ++i) m.push_back(make_pair(height[i], i + 1));

        //sort(m.begin(), m.end(), [](pair<int, int> a, pair<int, int> b) {return a.first < b.first;});

        //for (int i = 0; i < n; ++i) printf("%d %d\n", m[i].first, m[i].second);

        /*
        for (int i = 0; i < n; ++i) {
            int ans = 0;
            for (int j = n - 1; j >= 0; --j) {
                int ca = min(m[i].first, m[j].first) * abs(m[j].second - m[i].second);
                if (ans > ca) break;
                ans = ca;
            }
            if (ans > ret) ret = ans;
        }
        */
        int p1 = 0, p2 = n - 1;
        while (p1 < p2) {
            int ans = 0;
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
