class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #分别初始化9个集合存储9行,9列,9宫
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                #计算值属于哪一个宫
                square_num = (r // 3) * 3 + c // 3
                if value == '.':
                    continue
                elif value in rows[r] or value in cols[c] or value in squares[square_num]:
                    return False
                else:
                    rows[r].add(value)
                    cols[c].add(value)
                    squares[square_num].add(value)
        return True
