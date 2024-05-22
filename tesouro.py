class Tesouro:
    def __init__(self, nome, localizacao, valor):
        self.nome = nome
        self.localizacao = localizacao
        self.valor = valor

    def efeito(self):
        pass  # Pode ser sobrescrito para diferentes efeitos
