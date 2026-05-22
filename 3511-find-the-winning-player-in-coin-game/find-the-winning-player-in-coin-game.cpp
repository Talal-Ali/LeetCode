class Solution {
public:
    string winningPlayer(int x, int y) {
        int n = min(x,y/4);
        if(n%2){return "Alice";}
        return "Bob";
    }
};