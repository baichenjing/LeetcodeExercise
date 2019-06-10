class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records = [0] * len(nums)
        for first in range(len(nums)):
            second = first + 1
            while second < len(nums):
                if nums[first] + nums[second] == target:
                    return first, second
                second = second + 1

