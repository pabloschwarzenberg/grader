class Taxon:
    def __init__(self,categoria,nombre,subcategorias=[]):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=subcategorias
    def __str__(self):
        return("{0},{1},{2}".format(self.nombre,self.subcategoria,self.categoria))
 
