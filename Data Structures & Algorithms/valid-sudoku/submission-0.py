class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # define what rows, cols, and squares are:
        for i in range(len(board)): ##should be nine
            row = board[i]
            col = [board[j][i] for j in range(len(board))]
            topRow, topCol = (i // 3) * 3, (i % 3) * 3
            square = self.getSquare(board, topRow, topCol)
            print(row, col, square)
            if not self.checkValid(row):
                return False
            if not self.checkValid(col):
                return False
            if not self.checkValid(square):
                return False

        return True


    def getSquare(self, board, topRow, topCol):
        return board[topRow][topCol:topCol+3] + board[topRow + 1][topCol:topCol+3] + board[topRow+2][topCol:topCol+3]

    def checkValid(self, someList):
        valid = set([str(i) for i in range(1, 10)])
        valid.add(".")
        seen = set()
        for element in someList:
            if element not in valid:
                return False
            if element in seen and element != ".":
                return False
            else:
                seen.add(element)
        return True


        
        