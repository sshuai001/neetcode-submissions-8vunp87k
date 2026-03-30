class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue
                # r * n + c
                block_num = (r // 3) * 3 + (c // 3)
                
                if value in row[r] or value in col[c] or value in block[block_num]:
                    return False
                else:
                    row[r].add(value)
                    col[c].add(value)
                    block[block_num].add(value)
        return True