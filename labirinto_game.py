import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

from aventureiro import Aventureiro
from tesouro import Tesouro
from perigo import Perigo
from labirinto import Labirinto

class LabirintoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Labirinto Game")

        self.level = 1
        self.aventureiro = Aventureiro("Jogador1")
        self.labirinto = Labirinto()

        self.setup_ui()
        self.desenhar_labirinto()

    def setup_ui(self):
        self.label = tk.Label(self.root, text=f"Level: {self.level}")
        self.label.pack()

        self.next_level_button = tk.Button(self.root, text="Next Level", command=self.next_level)
        self.next_level_button.pack()

        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

    def desenhar_labirinto(self):
        self.canvas.delete("all")  # Limpa o canvas
        cell_size = 50  # Tamanho de cada célula do labirinto
        for y, row in enumerate(self.labirinto.estrutura):
            for x, cell in enumerate(row):
                color = "white" if cell == 0 else "black"
                self.canvas.create_rectangle(
                    x * cell_size, y * cell_size,
                    (x + 1) * cell_size, (y + 1) * cell_size,
                    fill=color
                )

    def next_level(self):
        self.level += 1
        self.label.config(text=f"Level: {self.level}")
        self.labirinto = Labirinto()  # Gerar novo labirinto
        self.desenhar_labirinto()

        if self.level == 10:
            self.show_easter_egg()

    def show_easter_egg(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Easter Egg")

        self.canvas_egg = tk.Canvas(self.top, width=500, height=500)
        self.canvas_egg.pack()

        # Carregar o GIF localmente
        self.gif_path = "easter_egg.gif"
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(self.gif_path))]

        self.image_index = 0
        self.update_image()

    def update_image(self):
        self.canvas_egg.create_image(250, 250, image=self.sequence[self.image_index])
        self.image_index = (self.image_index + 1) % len(self.sequence)
        self.root.after(50, self.update_image)  # Atualiza a cada 50ms para criar a animação do GIF
