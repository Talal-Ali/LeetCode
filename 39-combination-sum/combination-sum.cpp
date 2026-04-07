class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int i =0;
        vector<vector<int>> result;
        vector<int>set;
        helper(result, set, candidates, target, i);
        return result;

    }
    void helper(vector<vector<int>>& result,vector<int>&set, vector<int>& can, int target, int i)
    {
        if(target == 0)
        {
            result.push_back(set);
            return;
        }
        if (i >= can.size() || target < 0)
            return;
        set.push_back(can[i]);
        helper(result, set,can, target-can[i], i);
        set.pop_back();
        helper(result, set,can, target, i+1);
        
        return;
    }
};