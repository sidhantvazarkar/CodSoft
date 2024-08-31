# tic_tac_toe_tkinter.py

import tkinter as tk
from tkinter import messagebox
import numpy as np

# Initialize game board
BOARD_ROWS = 3
BOARD_COLS = 3
board = np.full((BOARD_ROWS, BOARD_COLS), '')

# AI Player (X) and Human Player (O)
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'

# Initialize tkinter window
window = tk.Tk()
window.title('Tic Tac Toe')

# Create buttons for the board
buttons = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def check_win(player):
    """Check if a player has won."""
    for row in range(BOARD_ROWS):
        if np.all(board[row, :] == player):
            return True
    for col in range(BOARD_COLS):
        if np.all(board[:, col] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def minimax(board, depth, is_maximizing):
    """Minimax algorithm for the AI to choose the best move."""
    if check_win(AI_PLAYER):
        return 1
    elif check_win(HUMAN_PLAYER):
        return -1
    elif np.all(board != ''):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == '':
                    board[row][col] = AI_PLAYER
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == '':
                    board[row][col] = HUMAN_PLAYER
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ''
                    best_score = min(score, best_score)
        return best_score

def best_move():
    """Find the best move for the AI."""
    best_score = float('-inf')
    move = (0, 0)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                board[row][col] = AI_PLAYER
                score = minimax(board, 0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def make_move(row, col, player):
    """Make a move on the board and update the button text."""
    if board[row][col] == '':
        board[row][col] = player
        buttons[row][col].config(text=player)
        if check_win(player):
            messagebox.showinfo("Game Over", f"{player} wins!")
            reset_board()
        elif np.all(board != ''):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            return True  # Continue game
    return False  # Invalid move

def human_move(row, col):
    """Handle human move and then trigger AI move."""
    if make_move(row, col, HUMAN_PLAYER):
        # AI move after human
        ai_row, ai_col = best_move()
        make_move(ai_row, ai_col, AI_PLAYER)

def reset_board():
    """Reset the game board."""
    global board
    board = np.full((BOARD_ROWS, BOARD_COLS), '')
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            buttons[row][col].config(text='')

# Create board buttons
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        buttons[row][col] = tk.Button(window, text='', font=('Arial', 40), width=5, height=2,
                                      command=lambda r=row, c=col: human_move(r, c))
        buttons[row][col].grid(row=row, column=col)

# Restart button
restart_button = tk.Button(window, text='Restart', font=('Arial', 20), command=reset_board)
restart_button.grid(row=BOARD_ROWS, column=0, columnspan=BOARD_COLS)

# Start the tkinter main loop
window.mainloop()
