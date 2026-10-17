class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     total = 0
    #     length = len(digits)
    #     for i in range(length):
    #         total += digits[i] * (10 ** (length - 1 - i))
    #     total += 1
    #     result = list()
    #     while total > 0:
    #         curr = total % 10
    #         result.append(curr)
    #         total //= 10
    #     result.reverse()
    #     return result

    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                #we know that we need to carry
                digits[i] = 0
        return [1] + digits

    