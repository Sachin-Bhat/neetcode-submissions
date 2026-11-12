class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # need a pointer k to track where the next valid element should go
        k = 0
        # iterate through array with index i
        for i in range(len(nums)):
            '''
            if nums[i] is not equal to val
            copy it to nums[k]
            and increment k
            '''
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k