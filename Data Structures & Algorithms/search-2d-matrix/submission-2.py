class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we could think of this like a big long list:
        numRows, numCols = len(matrix), len(matrix[0])
        lo, hi = 0, numRows * numCols #hi is not included

        while lo < hi:
            mid = lo + (hi - lo)//2
            midValue = matrix[mid // numCols][mid % numCols]

            if target == midValue:
                return True
            elif target < midValue:
                hi = mid
            else: 
                #assert that target > mid
                lo = mid + 1

        return False
            
        