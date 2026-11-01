from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hash_s = dict(Counter(s))
            hash_t = dict(Counter(t))
            if hash_s == hash_t:
                return True
        return False
