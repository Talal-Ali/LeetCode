class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxi = 0
        n = len(nums)
        for i in range(n):
            key = nums[i]%n
            if nums[i] == 1:
                count +=1
                if count > maxi:
                    maxi = count
            if nums[i] == 0:
                count = 0
        return maxi
        