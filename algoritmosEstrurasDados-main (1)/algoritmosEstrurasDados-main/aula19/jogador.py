class Jogador:
    def __init__(self, nome, numero_da_camisa, posicao, proximo):
        self.nome = nome 
        self.numero_da_camisa = numero_da_camisa
        self.__posicao = posicao
        self.proximo = proximo
    
    def __str__(self):
        return f"Numero:{self.nome} Nome:{self.numero_da_camisa} Posição{self.__posicao}"
    
    