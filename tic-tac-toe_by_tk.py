import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x450")
        self.master.configure(bg='#E0F7FA')
        self.current_player = 'X'
        self.board = [''] * 9
        self.buttons = []

        self.frame = tk.Frame(master, bg='#E0F7FA', padx=10, pady=10)
        self.frame.pack(expand=True)

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text='', font=('Roboto', 20, 'bold'), width=5, height=2,
                                command=lambda row=i, col=j: self.make_move(row, col),
                                bg='#FFFFFF', activebackground='#B2EBF2', relief=tk.FLAT, borderwidth=2)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        self.status_label = tk.Label(master, text="Player X's turn", font=('Roboto', 14), bg='#E0F7FA', fg='#00796B')
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(master, text="New Game", font=('Roboto', 12), command=self.reset_game,
                                    bg='#00796B', fg='white', activebackground='#004D40', relief=tk.FLAT, padx=10, pady=5)
        self.reset_button.pack(pady=10)

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg='#D32F2F' if self.current_player == 'X' else '#1976D2')
            if self.check_winner():
                self.highlight_winning_combination()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O'
                self.status_label.config(text="Computer's turn")
                self.master.after(500, self.computer_move)

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == '']
        if available_moves:
            move = self.get_best_move()
            self.board[move] = 'O'
            self.buttons[move].config(text='O', fg='#1976D2')
            if self.check_winner():
                self.highlight_winning_combination()
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'X'
                self.status_label.config(text="Player X's turn")

    def get_best_move(self):
        available_moves = [i for i in range(9) if self.board[i] == '']
        for move in available_moves:
            self.board[move] = 'O'
            if self.check_winner():
                self.board[move] = ''
                return move
            self.board[move] = ''
        for move in available_moves:
            self.board[move] = 'X'
            if self.check_winner():
                self.board[move] = ''
                return move
            self.board[move] = ''
        if 4 in available_moves:
            return 4
        corners = [0, 2, 6, 8]
        available_corners = [move for move in corners if move in available_moves]
        if available_corners:
            return random.choice(available_corners)
        return random.choice(available_moves)

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def highlight_winning_combination(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                for index in combo:
                    self.buttons[index].config(bg='#A5D6A7')
                break

    def reset_game(self):
        self.current_player = 'X'
        self.board = [''] * 9
        for button in self.buttons:
            button.config(text='', bg='#FFFFFF', fg='black')
        self.status_label.config(text="Player X's turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
