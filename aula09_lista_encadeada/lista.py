from no import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, valor):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = No( valor )
        else:
            self.inicio = No(valor)
        self.tamanho = self.tamanho + 1
        self.imprimir()
            

    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia")
        
        aux = self.inicio
        while(aux):
            print(aux.dado,"\n")
            aux = aux.proximo 
            print("Tamanho da Lista:" + str(self.tamanho))
    
    def excluir(self, valor):
        if self.tamanho == 0:
            print("A lista está vazia")
        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print("Valor não encontrado")
        else:
            ant = self.inicio
            aux = ant.proximo
            while(aux):
                if aux.dado == valor:
                    ant.proximo = aux.proximo
                    self.tamanho -= 1
                else:
                    ant = aux
                    aux = aux.proximo