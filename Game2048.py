# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import random

# Constants
BOARD_SIZE = 4
CELL_SIZE = 100
PADDING = 8
BG_COLOR = "#faf8ef"
EMPTY_COLOR = "#cdc1b4"

TILE_COLORS = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}
CURRENT_TILE_COLOR = "#ff0000"

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.geometry("540x540")
        self.window.resizable(False, False)
        self.window.bind("<Key>", self.handle_keypress)

        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.score = 0
        self.game_over = False
        self.current_tile = None

        self.cell_size = CELL_SIZE
        self.padding = PADDING

        self.canvas_width = self.cell_size * BOARD_SIZE + 2 * self.padding
        self.canvas_height = self.cell_size * BOARD_SIZE + 2 * self.padding

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.score_label = tk.Label(self.window, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg=BG_COLOR)
        self.canvas.pack()

    def start_game(self):
        self.create_tile()
        self.create_tile()
        self.update_board()

    def create_tile(self):
        empty_cells = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 2, 2, 4])

    def update_board(self):
        self.canvas.delete("tile")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = self.board[i][j]
                x, y = j * self.cell_size + self.padding, i * self.cell_size + self.padding
                color = TILE_COLORS.get(value, EMPTY_COLOR)
                if (i, j) == self.current_tile:
                    color = CURRENT_TILE_COLOR
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill=color, tags="tile")
                if value != 0:
                    self.canvas.create_text(x + self.cell_size / 2, y + self.cell_size / 2, text=str(value), font=("Helvetica", 18, "bold"), tags="tile")

        self.score_label.config(text="Score: " + str(self.score))

    def merge_tiles(self, row):
        merged_row = []
        i = 0
        while i < BOARD_SIZE:
            if i < BOARD_SIZE - 1 and row[i] == row[i + 1]:
                merged_value = 2 * row[i]
                self.score += merged_value
                merged_row.append(merged_value)
                i += 2
            else:
                merged_row.append(row[i])
                i += 1

        merged_row += [0] * (BOARD_SIZE - len(merged_row))
        return merged_row

    def merge_left(self):
        merged_board = []
        for row in self.board:
            merged_row = self.merge_tiles(row)
            merged_board.append(merged_row)
        self.board = merged_board

    def merge_right(self):
        merged_board = []
        for row in self.board:
            merged_row = self.merge_tiles(row[::-1])[::-1]
            merged_board.append(merged_row)
        self.board = merged_board

    def merge_up(self):
        transposed = [[self.board[j][i] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        merged_board = []
        for row in transposed:
            merged_row = self.merge_tiles(row)
            merged_board.append(merged_row)
        self.board = [[merged_board[j][i] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    def merge_down(self):
        transposed = [[self.board[j][i] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        merged_board = []
        for row in transposed:
            merged_row = self.merge_tiles(row[::-1])[::-1]
            merged_board.append(merged_row)
        self.board = [[merged_board[j][i] for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    def handle_keypress(self, event):
        if self.game_over:
            return

        if event.keysym in ("Left", "a"):
            self.current_tile = None
            self.merge_left()
        elif event.keysym in ("Right", "d"):
            self.current_tile = None
            self.merge_right()
        elif event.keysym in ("Up", "w"):
            self.current_tile = None
            self.merge_up()
        elif event.keysym in ("Down", "s"):
            self.current_tile = None
            self.merge_down()
        else:
            return

        self.create_tile()
        self.update_board()

        if self.is_game_over():
            self.game_over = True
            self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text="Game Over", font=("Helvetica", 32, "bold"), fill="red")

    def is_game_over(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == 0 or self.is_adjacent_match(i, j):
                    return False
        return True

    def is_adjacent_match(self, i, j):
        value = self.board[i][j]
        if i > 0 and self.board[i - 1][j] == value:
            return True
        if i < BOARD_SIZE - 1 and self.board[i + 1][j] == value:
            return True
        if j > 0 and self.board[i][j - 1] == value:
            return True
        if j < BOARD_SIZE - 1 and self.board[i][j + 1] == value:
            return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game2048()
    game.run()
    
    
    
    
    