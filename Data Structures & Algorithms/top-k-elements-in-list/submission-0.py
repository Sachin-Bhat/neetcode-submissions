from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = dict(Counter(nums))
        return heapq.nlargest(k, num_counts, key=num_counts.get)