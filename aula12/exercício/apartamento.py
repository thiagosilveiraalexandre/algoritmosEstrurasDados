class Apartamento:
    def __init__(self, id, numero, vaga, ap):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.proximo = ap
    
    def cadastrar(self, id , numero , vaga , ap):
        self.id = id 
        self.numero = numero 
        self.vaga = vaga 
        self.proximo = ap

    def imprimir(self):
        pass