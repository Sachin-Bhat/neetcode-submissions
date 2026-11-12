class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # need 2 variables
        ones, max_ones = 0, 0
        for num in nums:
            if num == 1:
                ones += 1
            if num == 0:
                ones = 0
            if max_ones < ones:
                max_ones = ones
        return max_ones