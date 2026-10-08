class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        lo, hi = 0, length
        while (lo<hi):
            mid = lo + (hi - lo)//2
            if nums[mid] == target: return mid
            elif target < nums[mid]:
                hi = mid
            else:
                # assert(target > nums[mid])
                lo = mid + 1
        return -1



        