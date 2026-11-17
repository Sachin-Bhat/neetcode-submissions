class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        Intuition
        ---------
        probably have a counter that holds the count subarray that match the condition
        have a left and right pointer the size of the window k
        '''
        res = 0
        L = 0
        window_sum = 0
        target = k * threshold

        for R in range(len(arr)):
            window_sum += arr[R]
            if R - L + 1 == k:
                if window_sum >= target:
                    res += 1
                window_sum -= arr[L]
                L += 1
        return res