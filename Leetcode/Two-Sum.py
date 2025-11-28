class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def toSum(self):
        """
        Return indices of the two numbers that add up to target.

        >>> Solution([2,7,11,15], 9).twoSum()
        [0, 1]

        >>> Solution([3,2,4], 6).twoSum()
        [1, 2]

        >>> Solution([3,3], 6).twoSum()
        [0, 1]
        """
        hashmap = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if  complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[num] = i


