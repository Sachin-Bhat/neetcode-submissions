class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(numbers, 1):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx
        return []