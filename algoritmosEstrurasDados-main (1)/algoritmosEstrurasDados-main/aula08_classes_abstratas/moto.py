from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo = None, ano = None ,cilindradas = 8):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas
    
    def imprimir(self):
        print("Motocicleta:")
        super().imprimir()
    
    def imprimirEspecifico(self):
        super().imprimirEspecifico()
        print("Cilindradas: " + str(self.cilindradas))