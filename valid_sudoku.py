class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    board[i][j] = int(board[i][j])
        # Rows
        for row in board:
            counts = [0] * 9
            for num in row:
                if num == ".":
                    continue
                counts[num - 1] += 1
            
            for num in counts:
                if num > 1:
                    return False
        
        # Cols
        for i in range(9):
            counts = [0] * 9
            for j in range(9):
                if board[j][i] == ".":
                    continue
                counts[board[j][i] - 1] += 1
            
            for num in counts:
                if num > 1:
                    return False

        # Grid
        squares = {(i, j): [] for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                new = (i // 3, j // 3)
                squares[new].append(board[i][j])

        
        for nums in list(squares.values()):
            for num in nums:
                if num != "." and nums.count(num) > 1:
                    return False

        return True