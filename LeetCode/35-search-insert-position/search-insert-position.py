class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while (lo < hi):
            mid = lo + (hi - lo)//2
            curr = nums[mid]
            if curr == target:
                return mid
            elif target < curr:
                #we need to search the first half
                hi = mid
            else:
                assert(target > curr)
                lo = mid + 1
        return lo


        [1, 2, 4, 5, 6]
        