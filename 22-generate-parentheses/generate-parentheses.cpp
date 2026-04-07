class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string s = "";
        vector<string> result;
        int right = 0;
        int left = 0;
        helper(n, result, s,right,left);
        return result;
    }
    void helper(int n,vector<string>& result, string s, int right, int left)
    {
        if(s.size() == n*2){
            result.push_back(s);    
            return;
        }
        if(left<n){ helper(n, result, s + "(",right, left+1 );}
        if(right<left){helper(n, result, s + ")", right+1, left);}
    }
};