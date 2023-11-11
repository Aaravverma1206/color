import tkinter as tk
from random import choice

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Identifying Game")

        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]
        self.font_colors = ["white", "black", "gray", "cyan", "magenta", "brown", "lime", "maroon"]

        self.color_name_label = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.color_name_label.pack(pady=20)

        self.next_button = tk.Button(self.root, text="Next Color", command=self.next_color)
        self.next_button.pack()

        self.next_color()

    def next_color(self):
        random_color = choice(self.colors)
        random_font_color = choice(self.font_colors)

        self.color_name_label.config(text=random_color, fg=random_font_color)

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
