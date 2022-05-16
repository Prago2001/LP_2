import time
class NQueens_Branch_Bound:
    def __init__(self) -> None:
        self.size = int(input("Enter size of chessboard"))
        self.board = [[False]*self.size for _ in range(self.size)]
        self.columns = [False] * self.size
        self.count = 0
        # There will 2 * n - 1 diagonals on the board
        # fsDiagonal = Forward Slash Diagonal
        self.fsDiagonal = [False] * (2 * self.size - 1)
        # bsDiagonal = Backward Slash Diagonal
        self.bsDiagonal = [False] * (2 * self.size - 1)

    def printBoard(self):
        for row in self.board:
            for ele in row:
                if ele == True:
                    print("Q",end=" ")
                else:
                    print("X",end=" ")
            print()
        print()
    
    def isSafe(self,row:int,col:int) -> bool:
        fsTotal = row + col
        bsTotal = row - col + self.size - 1
        if self.columns[col] == False and self.fsDiagonal[fsTotal] == False and self.bsDiagonal[bsTotal] == False:
            return True
        return False
    
    def solve(self,row:int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return
        
        for col in range(self.size):
            if self.isSafe(row,col) == True:
                self.board[row][col] = True
                self.columns[col] = True
                fsTotal = row + col
                bsTotal = row - col + self.size - 1
                self.fsDiagonal[fsTotal] = True
                self.bsDiagonal[bsTotal] = True

                self.solve(row + 1)

                self.board[row][col] = False
                self.columns[col] = False
                self.fsDiagonal[fsTotal] = False
                self.bsDiagonal[bsTotal] = False
        
solver = NQueens_Branch_Bound()
start = time.time()
solver.solve(0)
print(solver.count)
print(f"Time taken: {time.time() - start}")

