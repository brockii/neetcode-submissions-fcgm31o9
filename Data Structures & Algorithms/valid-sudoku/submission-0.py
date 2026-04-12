class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):

                # no need to something about blank spaces
                if board[i][j] == ".":
                    continue

                # get the number
                number = board[i][j]

                row = board[i]
                column = [r[j] for r in board]
                

                row_portion_to_check = row[:j] + row[j+1:]
                if number in row_portion_to_check:
                    return False
                column_portion_to_check = column[:i] + column[i+1:]
                if number in column_portion_to_check:
                    return False
                
                row_start = (i // 3) * 3
                column_start = (j // 3) * 3

                for y in range(row_start, row_start+3):
                    for z in range(column_start, column_start+3):
                        if (y,z) == (i,j) or board[y][z] == ".":
                            continue
                        if number == board[y][z]:
                            return False
        return True