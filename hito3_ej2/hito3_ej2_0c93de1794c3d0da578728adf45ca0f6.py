class Taxon:
    def __init__(self,c,n, subcategorias=[]):
        self.categoria=c
        self.nombre=n
        self.subcategorias=subcategorias

    def incluir(self, orden):
        self.subcategorias.append(orden)
      