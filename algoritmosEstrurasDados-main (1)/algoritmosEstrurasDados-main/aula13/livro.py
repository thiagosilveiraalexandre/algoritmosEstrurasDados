class Livro:
    def __init__(self, titulo ,autor , pg):
        self.titulo = titulo 
        self.autor = autor 
        self.paginas = pg
        self.proximo = None
    
    def __str__(self) -> str:
        texto = "-------------------"
        texto += "\nTítulo: " + self.titulo
        texto += "\nAutor: "  + self.autor 
        texto += "\nPáginas: " + str(self.paginas)
        return texto 