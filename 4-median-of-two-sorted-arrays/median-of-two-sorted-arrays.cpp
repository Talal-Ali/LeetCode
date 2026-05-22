class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums3;
        for(int i=0; i<size(nums1); i++)
        {
            nums3.push_back(nums1[i]);
        }
        for(int i=0; i<size(nums2); i++)
        {
            nums3.push_back(nums2[i]);
        }
        sort(nums3.begin(), nums3.end()); 
        int s = size(nums3);
        if(s%2 == 1)
        {
            return (double)nums3[s/2];
        }
        else {
            return (((double)nums3[s/2 -1] + (double)nums3[(s/2)]) / 2);
        }
    }
};