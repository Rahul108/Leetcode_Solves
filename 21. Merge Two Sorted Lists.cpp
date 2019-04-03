/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dm(0);
        auto tpr = &dm;
        while(l1 && l2){
            auto &val = (l1->val < l2->val) ? l1 : l2;
            tpr->next = val;
            tpr = val;
            val = val -> next;
        }
        tpr->next = l1 ? l1 : l2;
        return dm.next;
    }
};
