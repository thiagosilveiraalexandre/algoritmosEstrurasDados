from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = None, ano = None, qtdPortas = 4):
        super().__init__(modelo, ano)
        self.qtdPortas = qtdPortas
    
    def imprimir(self):
        print("Carrão")
        super().imprimir()
    
    def imprimirEspecifico(self):
        super().imprimirEspecifico()
        print("Quantidade de Portas:" + str(self.qtdPortas))