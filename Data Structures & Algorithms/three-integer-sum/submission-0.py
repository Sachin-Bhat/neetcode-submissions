class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        '''
        Intuition
        ---------
        After sorting the array, we can fix one number and search the other 2 using the two-pointer approach.
        Sorting helps:
        1. skip duplicates easily.
        2. ensure that moving the left or right pointer will increase or decrease the sum in a predictable way.

        For each fixed number a, we place 2 pointers
        - l, starts just after index i
        - r, start at the end

        So basically, if current sum is too large -> move r left to reduce it.
        Conversely, if sum is too small -> move l right to increase it.

        When sum is 0 -> record the triplet and skip duplicates.
        '''

        for i, a in enumerate(nums):
            if a > 0: # early exit, after sort a is the smallest element
                break
            
            if i > 0 and a == nums[i - 1]: # skip repeated 1st element
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # record triplet
                    l += 1 # move pointers inward
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # skip duplicates for nums[l]
        return res
