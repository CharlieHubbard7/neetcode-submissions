class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        count = 1
        copy = n
        while (copy > 1):
            count += copy % 2
            copy //= 2
        return count