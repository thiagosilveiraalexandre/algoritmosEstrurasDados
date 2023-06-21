from fila import Fila
class Torre:
    def __init__(self, id, nome, end):
        self.id = id
        self.nome = nome
        self.endereco = end
    
    def cadastrar(self, id , nome, end):
        self.id = id 
        self.nome = nome 
        self.endereco = end
    
    