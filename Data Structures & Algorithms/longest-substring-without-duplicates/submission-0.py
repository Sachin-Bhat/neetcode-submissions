class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Intuition
        ---------
        we need length and max_length to keep track of substring lengths

        Early exit conditions:
        1. empty string or single character -> retrurn len(s)

        we can try using sliding window
        update conditions:
        R automatically increases every iteration (for)
        keep L increasing when a dupe is reached
        record and update counts
        '''
        length, max_length = 0, 0
        L = 0

        if s == "" or len(s) == 1:
            return len(s)
        
        for R in range(len(s)):
            while s[R] in s[L:R]:
                L += 1
            length = R - L + 1
            if length > max_length:
                max_length = length
        return max_length
