class Solution:
    def trap(self, height: list[int]) -> int:
        '''
        Intuition
        ----------
        Before looking at anything let us look at if there are any early exit cases

        1. Empty height array -> return 0

        We use the 2-pointer approach
        - we can initialise pointers l and r on either ends of the array
        - we also need something to keep a track of the maximum of l and r each
        - we also need a res list to store the result over the iterations

        Basically we need to count the blue squares (water)
        - water depend on the shorter wall
        
        Pointer update conditions
        -------------------------
        Note: if left wall is shorter than right -> we can safely shift l to the right (also consider max update and add to result blue height)
        else if reverse is true -> shift r to the left and do the same
        '''
        if len(height) == 0:
            return 0
        
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[len(height) - 1]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res