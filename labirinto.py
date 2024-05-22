import random

class Labirinto:
    def __init__(self, largura=10, altura=10):
        self.largura = largura
        self.altura = altura
        self.estrutura = self.gerar_labirinto()
        self.tesouros = []
        self.perigos = []

    def gerar_labirinto(self):
        # Gera uma matriz 10x10 de 0s (representando caminhos) e 1s (representando paredes)
        labirinto = [[random.choice([0, 1]) for _ in range(self.largura)] for _ in range(self.altura)]
        return labirinto

    def adicionar_tesouro(self, tesouro):
        self.tesouros.append(tesouro)

    def remover_tesouro(self, tesouro):
        self.tesouros.remove(tesouro)

    def adicionar_perigo(self, perigo):
        self.perigos.append(perigo)

    def remover_perigo(self, perigo):
        self.perigos.remove(perigo)
