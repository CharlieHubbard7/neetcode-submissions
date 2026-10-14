class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroIndexes = set()
        countZeroes = 0
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.add(i)
                countZeroes += 1
            else:
                total *= nums[i]
        
        for i in range(len(nums)):
            if countZeroes == 0:
                result[i] = int(total / nums[i])
            elif countZeroes == 1:
                if i in zeroIndexes:
                    result[i] = total
                else: 
                    result[i] == 0
            else: 
                result[i] == 0

        return result
            