from no import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionarInicio(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo 
            self.fim = nodo 
        else:
            nodo.proximo = self.inicio 
            self.inicio.anterior = nodo 
            self.inicio = nodo 
        self.tamanho += 1
        self.imprimir()
    
    def addNoFim(self,valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo 
            self.fim = nodo
        else:
            self.fim.proximo = nodo 
            nodo.aanterior = self.fim
            self.fim = nodo 
        self.tamanho +=1
        self.imprimir()
        
    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia")
        else: 
            aux = self.inicio
            while(aux):
                print(aux.dado,"\n")
                aux = aux.proximo 
            print("Tamanho da Lista:" + str(self.tamanho))
    
    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista Vazia!")
            return
        elif self.inicio.proximo == None:
            self.inicio = None
            self.fim = None 
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None 
            self.tamanho -=1
        self.imprimir()
    
    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia!")
            return
        elif self.inicio.proximo == None:
            self.inicio = None
            self.fim = None 
            self.tamanho = 0
        else:
            self.fim = self.fim.anterior 
            self.fim.proximo = None
            self.tamanho -=1
        self.imprimir()
    
    
    def imprimirReverso(self):
        if self.inicio == None:
            print("Lista vazia!")
        else:
            aux = self.fim
            while(aux):
                print(aux.dado,"\n")
                aux = aux.anterior
            print("Tamanho da Lista:" + str(self.tamanho))