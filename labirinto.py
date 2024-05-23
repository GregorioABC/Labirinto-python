import random

class Labirinto:
    def __init__(self, largura=10, altura=10):
        self.largura = largura
        self.altura = altura
        self.estrutura = self.gerar_labirinto()
        self.tesouros = []
        self.perigos = []
        self.inicio = (0, 0)
        self.fim = (largura - 1, altura - 1)

    def gerar_labirinto(self):
        labirinto = [[random.choice([0, 1]) for _ in range(self.largura)] for _ in range(self.altura)]
        labirinto[0][0] = 0  # Assegura que o ponto inicial seja um caminho
        labirinto[self.altura - 1][self.largura - 1] = 0  # Assegura que o ponto final seja um caminho
        return labirinto

    def adicionar_tesouro(self, tesouro):
        self.tesouros.append(tesouro)

    def remover_tesouro(self, tesouro):
        self.tesouros.remove(tesouro)

    def adicionar_perigo(self, perigo):
        self.perigos.append(perigo)

    def remover_perigo(self, perigo):
        self.perigos.remove(perigo)