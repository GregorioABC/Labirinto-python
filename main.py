import subprocess
import sys

# Certifique-se de que a biblioteca Pillow está instalada
try:
    from PIL import Image, ImageTk, ImageSequence
except ImportError:
    print("Pillow não está instalado. Instalando agora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageTk, ImageSequence

import tkinter as tk
from labirinto_game import LabirintoGame

if __name__ == "__main__":
    root = tk.Tk()
    game = LabirintoGame(root)
    root.mainloop()
