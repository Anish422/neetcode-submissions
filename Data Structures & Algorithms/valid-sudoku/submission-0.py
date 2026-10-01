class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                r = i // 3
                c = j // 3
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(r,c)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(r,c)].add(board[i][j])
        
        return True


