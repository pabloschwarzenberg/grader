class Taxon:
    def __init__(self, categoria, nombre,subcategorias=[]):
        self.categoria = categoria 
        self.nombre = nombre
        self.subcategorias=subcategorias
    def darcategoria(self):
        return self.categoria
    def darnombre(self):
        return self.nombre
    def darsubcategorias(self):
        return self.subcategorias