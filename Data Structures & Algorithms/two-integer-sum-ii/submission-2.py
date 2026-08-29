class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, curr in enumerate(numbers):
            needed = target - curr

            if needed in seen:
                return [seen[needed] + 1, i + 1]

            seen[curr] = i