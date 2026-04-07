class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1 = []
        for i in range(n):
            nums1.append(nums[i])
            nums1.append(nums[i+n])
        return nums1
        
