class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retlist = []
        for i in range(0, 2 * len(nums)):
            retlist.append(nums[i % len(nums)])
        return retlist
        