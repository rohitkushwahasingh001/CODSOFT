import random

# Constants for representing the players and the board
X = "X"
O = "O"
EMPTY = " "
board = [EMPTY for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i + 1]} | {board[i + 2]} |")
        print("-------------")

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return EMPTY not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, X):
        return -1
    if check_winner(board, O):
        return 1
    if is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move for the AI player
def best_move(board):
    best_eval = float("-inf")
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = O
            eval = minimax(board, 0, False, float("-inf"), float("inf"))
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main function to run the Tic-Tac-Toe game
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(list(range(1, 10)))
    while True:
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] != EMPTY or not 0 <= player_move <= 8:
            print("Invalid move. Please try again.")
            continue
        
        board[player_move] = X
        print_board(board)
        
        if check_winner(board, X):
            print("Congratulations! You win!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        ai_move = best_move(board)
        board[ai_move] = O
        print("AI's move:")
        print_board(board)
        
        if check_winner(board, O):
            print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
