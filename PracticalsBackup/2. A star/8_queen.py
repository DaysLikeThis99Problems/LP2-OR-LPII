import heapq
import random
g=0

class State:
    def __init__(self, board, g_cost, h_cost):
        self.board = board  
        self.g_cost = g_cost  
        self.h_cost = h_cost  
        self.f_cost = g_cost + h_cost  

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def print_board(board):
    size = len(board)
    chessboard = [['.' for _ in range(size)] for _ in range(size)]
    
    for row in range(size):
        chessboard[row][board[row]] = 'Q' 
    
    for row in chessboard:
        print(" ".join(row))
    print()

def calculate_heuristic(board):
    size = len(board)
    attacks = 0
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def get_successors(board):
    size = len(board)
    successors = []
    
    for row in range(size):
        if board[row] == -1:  
            columns = list(range(size))
            random.shuffle(columns)  
            for col in columns:
                new_board = board[:]
                new_board[row] = col  
                successors.append(new_board)
    return successors

def solve_queens_a_star(start_state):
    open_list = []
    closed_list = set()
    
    initial_h = calculate_heuristic(start_state)
    initial_state = State(start_state, 0, initial_h)
    heapq.heappush(open_list, initial_state)
    
    while open_list:
        current_state = heapq.heappop(open_list)  
        current_board = current_state.board
        print_board(current_board)
        
        if current_state.h_cost == 0:  
            print("Solution found!")
            
            return
        
        closed_list.add(tuple(current_board))
        
        successors = get_successors(current_board)
        for successor in successors:
            if tuple(successor) not in closed_list:
                g_cost = current_state.g_cost + 1
                h_cost = calculate_heuristic(successor)
                successor_state = State(successor, g_cost, h_cost)
                heapq.heappush(open_list, successor_state)
    
    print("No solution found.")

def main():
    size = 8  
    start_state = [-1] * size  

#     print("Initial state:")
#     print_board(start_state)
    
    solve_queens_a_star(start_state)

if __name__ == "__main__":
    main()
