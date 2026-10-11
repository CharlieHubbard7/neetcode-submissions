class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxAreaTotal = 0
        while (left < right):
            area = self.calculateArea((right - left), heights[left], heights[right])
            maxAreaTotal = max(maxAreaTotal, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxAreaTotal


    def calculateArea(self, distance, height1, height2):
        heightUsed = min(height1, height2)
        return distance * heightUsed
        