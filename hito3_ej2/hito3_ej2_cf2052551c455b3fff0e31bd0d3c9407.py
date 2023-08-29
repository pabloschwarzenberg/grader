class Taxon:
    def __init__(self,categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

class Subcategoria(Taxon):
    def __init__(self, categoria, nombre, subcategoria):
        super().__init__(categoria, nombre)
    Subcategoria = []    
