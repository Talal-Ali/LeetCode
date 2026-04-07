class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        int n = nums.size();
        return (helper(nums, subset, result, n));
    }
    vector<vector<int>> helper(vector<int>& nums, vector<int>&subset, vector<vector<int>> &result,int n){

    
    if(subset.size() == n)
    {
        result.push_back(subset);
        return result;
    }
    for(int i = 0; i<n; i++)
    {
        if(find(subset.begin(), subset.end(), nums[i]) == subset.end())
        {
            subset.push_back(nums[i]);
            helper(nums, subset, result, n);
            subset.pop_back();
        }
    }
    return result;
    }
};