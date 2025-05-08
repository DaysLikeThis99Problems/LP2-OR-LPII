class nQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
            for j in range(self.n):
                if (self.board[i][j] == 1 and
                   (abs(i - row) == abs(j - col))):
                    return False
        return True

    def solve(self, row):
        if row == self.n:
            solution = []
            for i in range(self.n):
                row_solution = ''
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        row_solution += 'Q'
                    else:
                        row_solution += '.'
                solution.append(row_solution)
            self.solutions.append(solution)
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0  # Backtrack

    def print_solutions(self):
        if not self.solutions:
            print("No solutions found.")
        else:
            print(f"\nTotal solutions: {len(self.solutions)}\n")
            for solution in self.solutions:
                for row in solution:
                    print(row)
                print()


# Main Execution
if __name__ == '__main__':
    n = int(input("Enter the size of the chessboard: "))
    queens = nQueens(n)
    queens.solve(0)
    queens.print_solutions()


# shravanbobade@Shravans-Laptop 4. CSP % python n_queen.py
# Enter the size of the chessboard: 4

# Total solutions: 2

# .Q..
# ...Q
# Q...
# ..Q.

# ..Q.
# Q...
# ...Q
# .Q..