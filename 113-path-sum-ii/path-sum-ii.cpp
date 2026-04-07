/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> r;
        vector<vector<int>>r2;
        r2 = helper( root,targetSum,r,r2);
        return r2;
    }

    private:
        vector<vector<int>> helper(TreeNode* root, int targetSum, vector<int>& r,vector<vector<int>>&r2) {
        
        if(root == nullptr)
        {
            return r2;
        }
        r.push_back(root->val);
        if (!root->left && !root->right && targetSum == root->val)
        {
            r2.push_back(r);
        }
        helper(root->left, targetSum - root->val, r, r2);
        helper(root->right, targetSum - root->val, r, r2);
        r.pop_back();
        return r2;
    }
};