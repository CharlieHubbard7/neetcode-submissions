class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        seenAgain = set()
        for num in nums:
            if num not in seen: 
                seen.add(num)
            else:
                seenAgain.add(num)
        return seen.difference(seenAgain).pop()