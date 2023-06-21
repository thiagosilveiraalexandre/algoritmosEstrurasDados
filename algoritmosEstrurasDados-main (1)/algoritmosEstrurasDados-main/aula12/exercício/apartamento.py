from torre import Torre
#class Apartamento:
#    def __init__(self, id, numero, vaga, ap):
#        self.id = id
#        self.numero = numero
#        self.vaga = vaga
#        self.proximo = ap
    
#    def cadastrar(self, id , numero , vaga , ap):
#        self.id = id 
#        self.numero = numero 
#        self.vaga = vaga 
#        self.proximo = ap

#    def imprimir(self):
#        pass

class Apartamento:
    def __init__(self,id,nome,endereco,vaga,proximo):
        super().__init__( id, nome,endereco)
        vaga = vaga
        proximo = proximo
    
    def __str__(self):
        texto = "\n----------------------"
        texto += "\nNúmero: " + self.numero
        texto += "\nEndereco: " + self.torre .endereco
        return texto