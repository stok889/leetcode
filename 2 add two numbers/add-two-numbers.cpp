#include <bits/stdc++.h>

using namespace std;

const int INF = 0x3f3f3f3f;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void add(ListNode *r, int x) {
    while (1) {
        if (r->next != nullptr) {
            r = r->next;
        }
        else {
            r->next = new ListNode(x);
            break;
        }
    }
}
void print(ListNode *p) {
    while (1) {
        printf("%d\n", p->val);
        if (p->next == nullptr) break;
        p = p->next;
    }
}

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int r = 0, m = 0, f1 = 0, f2 = 0;
        int x = l1->val + l2->val;
        r = x % 10;
        m = x / 10;
        ListNode *ret = new ListNode(r);

        while (l1->next != nullptr || l2->next != nullptr) {
            if (l1->next != nullptr) l1 = l1->next;
            else f1 = 1;
            if (l2->next != nullptr) l2 = l2->next;
            else f2 = 1;

            x = (f1 == 0 ? l1->val : 0) + (f2 == 0 ? l2->val : 0) + m;
            r = x % 10;
            m = x / 10;

            add(ret, r);                
        }

        if (m != 0) add(ret, m);

        return ret;
    }
};

int main()
{
    printf("%d\n", INF);

    Solution s;
    ListNode *l1, *l2;

    l1 = new ListNode(2);
    add(l1, 4);
    add(l1, 3);
    print(l1);
    l2 = new ListNode(5);
    add(l2, 6);
    add(l2, 4);
    print(l2);
 
    ListNode *ans = s.addTwoNumbers(l1, l2);
    print(ans);

    delete l1;
    l1 = nullptr;

    delete l2;
    l2 = nullptr;

    delete ans;
    ans = nullptr;

    l1 = new ListNode(0);
    l2 = new ListNode(0);
    ans = s.addTwoNumbers(l1, l2);
    print(ans);

    delete l1;
    l1 = nullptr;

    delete l2;
    l2 = nullptr;

    delete ans;
    ans = nullptr;

    l1 = new ListNode(9);
    add(l1, 9);
    add(l1, 9);
    add(l1, 9);
    add(l1, 9);
    add(l1, 9);
    add(l1, 9);
    l2 = new ListNode(9);
    add(l2, 9);
    add(l2, 9);
    add(l2, 9);
    ans = s.addTwoNumbers(l1, l2);
    print(ans);

    return 0;
}
