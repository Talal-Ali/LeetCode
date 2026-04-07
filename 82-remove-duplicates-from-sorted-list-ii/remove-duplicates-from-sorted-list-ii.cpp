class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {

        if (!head) return nullptr;
        while (head && head->next && head->val == head->next->val)
        {
            int v = head->val;
            while (head && head->val == v)
            {
                ListNode* d = head;
                head = head->next;
                delete d;
            }
        }

        if (!head) return nullptr;

        ListNode* temp = head;

        while (temp && temp->next)
        {
            if (temp->next->next && temp->next->val == temp->next->next->val)
            {
                int v = temp->next->val;
                while (temp->next && temp->next->val == v)
                {
                    ListNode* d = temp->next;
                    temp->next = temp->next->next;
                    delete d;
                }
            }
            else
            {
                temp = temp->next;
            }
        }

        return head;
    }
};
