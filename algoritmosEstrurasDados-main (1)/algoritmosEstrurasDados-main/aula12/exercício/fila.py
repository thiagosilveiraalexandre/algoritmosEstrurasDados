from apartamento import Apartamento

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None 
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
        
    def add(self, apto):
#        nodo = No(valor)
        if self.primeiro == None:
            self.primeiro = apto 
            self.ultimo = apto  
        else:
            self.ultimo.proximo = apto 
            self.ultimo = apto 
        self.tamanho +=1
        self.imprimir()

    def imprimir(self):
        print("------------------------------")
        texto = ""
        if self.primeiro == None:
            texto = "Fila Vazia!"
            print(texto)
        else:
            aux = self.primeiro
            while(aux):
                print( aux )
                texto += aux.__str__()
                aux = aux.proximo 
            print("Tamanho da Fila:" + str(self.tamanho))
    
    def remover(self):
        aux = self.primeiro
        if self.tamanho == None:
            print("A Fila está vazia")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir() 
        if aux != None:
           aux.proximo = None
        return aux 