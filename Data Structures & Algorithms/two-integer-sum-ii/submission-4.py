class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, curr in enumerate(numbers):
            if target - curr in seen:
                return [seen[target - curr]+1, i+1]
            seen[curr] = i