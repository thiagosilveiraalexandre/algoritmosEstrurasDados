#from abc import ABCMeta
#from abc import ABC
from abc import ABC, abstractmethod
class Veiculo(metaclass=ABCMeta):
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano

    def imprimir (self):
        print("Modelo: " + self.modelo)
        print("Ano: " + str(self.ano))

    @abstractmethod
    def imprimirEspecifico(self):
        super().imprimir()
        print("Portas: " + self.qtdPortas)