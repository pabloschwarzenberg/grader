class Taxon:
    def __init__(self, categoria, nombre):
        self.subcategorias = []
        self.nombre = nombre
        self.categoria = categoria
    
    def incluir(self, x):
       self.subcategorias.append(x)