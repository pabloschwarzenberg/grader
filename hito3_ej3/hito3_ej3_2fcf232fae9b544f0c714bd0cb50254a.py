class Taxon:
    def __init__(self,c,n,subcategoria=[]):
        self.categoria=c
        self.nombre=n
        self.subcategorias=subcategoria
    def incluir(self,orden):
        self.subcategorias.append(orden)
      