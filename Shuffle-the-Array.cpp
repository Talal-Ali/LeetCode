1class Solution(object):
2    def shuffle(self, nums, n):
3        """
4        :type nums: List[int]
5        :type n: int
6        :rtype: List[int]
7        """
8        nums1 = []
9        for i in range(n):
10            nums1.append(nums[i])
11            nums1.append(nums[i+n])
12        return nums1
13        
14