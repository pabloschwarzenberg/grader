class Taxon:
    def __init__(self, categoria, nombre,subcategoria=[]):
        self.categoria = categoria 
        self.nombre = nombre
        self.subcategoria=subcategoria
    def darcategoria(self):
        return self.categoria
    def darnombre(self):
        return self.nombre
    def darsubcategoria(self):
        return self.subcategoria
      