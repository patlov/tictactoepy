import random
import tkinter as tk
from tkinter import font

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='grey')

        # set the font for the buttons
        self.button_font = font.Font(family="Comic Sans MS", size=20)

        self.board = [[None, None, None] for _ in range(3)]
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self.root, width=10, height=5, font=self.button_font, command=lambda i=i, j=j: self.move(i,j))
                button.grid(row=i, column=j, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
        self.player = "X"

        self.retry_button = tk.Button(self.root, text='Retry', command=self.restart_game, width=10, height=5, font=self.button_font) 
        self.retry_button.grid(row=1, column=3, padx=5, pady=5)
        self.retry_button.config(state='disabled')

        self.winner = tk.Label(self.root, text='', bg='grey')
        self.winner.grid(row=0, column=3, padx=5, pady=10)



    def move(self, i, j):
        if self.board[i][j] is not None:
            return
        self.board[i][j] = self.player
        if self.player == "X":
            self.buttons[i][j]["text"] = self.player
            self.buttons[i][j]["bg"] = '#3498db'
            self.buttons[i][j]["fg"] = '#ffffff'
            self.player = "O"
            if not self.is_game_over():
                self.ai_move()
        else:
            self.buttons[i][j]["text"] = self.player
            self.buttons[i][j]["bg"] = '#f1c40f'
            self.player = "X"

    def is_game_over(self):
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                self.end_game("Player " + self.getPrevPlayer() + " is the winner!")
                return True
        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                self.end_game("Player " + self.getPrevPlayer() + " is the winner!")
                return True
        
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.end_game("Player " + self.getPrevPlayer() + " is the winner!")
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.end_game("Player " + self.getPrevPlayer() + " is the winner!")
            return True

        # check for draw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        self.end_game("Its a Draw")
        return True


    def ai_move(self):
        self.root.after(500, self._ai_move)

    def _ai_move(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0,2)
            if self.board[i][j] is None:
                break
        self.board[i][j] = "O"
        self.buttons[i][j]["text"] = "O"
        self.buttons[i][j]["bg"] = "#f1c40f"
        self.player = "X"
        self.is_game_over()





    def getPrevPlayer(self):
        if self.player == 'X':
            return 'O'
        else:
            return 'X'


    def end_game(self, text_):
        self.winner.config(text=text_)
        self.disable_buttons()
        self.retry_button.config(state='normal')

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

    def restart_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.retry_button.config(state='disabled')
        self.winner.config(text="")
        self.player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='normal')
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["bg"] = "#ffffff"






if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
