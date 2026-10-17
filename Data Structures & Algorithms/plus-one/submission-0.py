class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        length = len(digits)
        for i in range(length):
            total += digits[i] * (10 ** (length - 1 - i))
        total += 1
        result = list()
        while total > 0:
            curr = total % 10
            result.append(curr)
            total //= 10
        result.reverse()
        return result


