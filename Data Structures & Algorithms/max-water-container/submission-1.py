class Solution:
    def maxArea(self, heights: list[int]) -> int:
        '''
        Intution
        --------
        Two-pointer approach
        where we initialise a variable to hold max area
        we have 2 pointers one at each end.

        Note: the width reduces over iterations

        To smartly shift pointers:
        if heights[l] < heights[r] -> we shift l to the right
        if heights[l] > heights[r] -> we shift r to the left
        otherwise both are shifted

        another thing to look at is updating area -> update if new area > old area
        '''

        max_area = -1
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area
