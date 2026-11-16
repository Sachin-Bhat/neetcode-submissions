class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter alphanumeric characters in lowercase and compare to its reverse
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]