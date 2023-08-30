
import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.sign_directory = [''] * 9
        self.index_list = []
        self.current_player = 'X'

        self.label = tk.Label(root, text="Tic Tac Toe")
        self.label.pack()

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.draw_board()
        
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100)
            self.canvas.create_line(i * 100, 0, i * 100, 300)

        for i, sign in enumerate(self.sign_directory):
            row = i // 3
            col = i % 3
            x = col * 100 + 50
            y = row * 100 + 50
            self.canvas.create_text(x, y, text=sign, font=("Helvetica", 32))
        
    def take_input(self, index):
        if index in self.index_list:
            messagebox.showinfo("Invalid Move", "This spot is blocked.")
            return

        self.index_list.append(index)
        self.sign_directory[index] = self.current_player
        self.draw_board()

        self.check_winner()
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        # ... (votre logique pour vérifier le gagnant) ...

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
