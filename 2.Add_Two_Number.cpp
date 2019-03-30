class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode pr(0), *n = &pr;
        int cr(0),sm;
        while(l1 != NULL || l2 != NULL || cr){
            int a1 = l1 ? l1->val : 0;
            int a2 = l2 ? l2->val : 0;
            sm = a1 + a2 + cr;
            n->next = new ListNode(sm%10);
            cr = sm/10;
            n = n->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return pr.next;
    }
};
