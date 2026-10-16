class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = None
        for row in grid:
            for v in row:
                if v in seen:
                    repeated = v
                seen.add(v)
        missing = (set(range(1, n * n + 1)) - seen).pop()
        return [repeated, missing]

        