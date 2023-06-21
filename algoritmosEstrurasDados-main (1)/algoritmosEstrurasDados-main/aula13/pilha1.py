from livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

#    def adicionar(self, valor):
#            aux = self.proximo
 #           while(aux.proximo):
   #             aux = aux.proximo
 #           aux.proximo = No( valor )
   #     else:
 #           self.proximo = No(valor)
    #    self.tamanho = self.tamanho + 1
    #    self.imprimir()
        
    def add(self,livro):
#        nodo = No(valor)
        livro = livro
        if self.topo == None:
            self.topo = livro 
        else:
            livro.proximo = self.topo
            self.topo = livro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("------------------------------")
        if self.topo == None:
            print("Pilha Vazia")
        else:
            aux = self.topo
            while(aux):
                print( aux )
                aux = aux.proximo 
            print( "Tamanho:" , str(self.tamanho))
    
    def remover(self):
        if self.topo == None:
            print("A Pilha está vazia")
        else: 
            self.topo = self.topo.proximo
            self.tamanho -=1
            self.imprimir() 