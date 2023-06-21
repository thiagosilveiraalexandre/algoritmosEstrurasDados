from livro import Livro 
from pilha1 import Pilha

l1 = Livro("A Rosa", "Cezar", 200)
l2 = Livro("Harry Potter", "J.K Rowling", 500)
l3 = Livro("O tempo e o vento", "Érico Verissimo", 200)

pilha = Pilha()
pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.imprimir()