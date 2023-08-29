class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        subcategorias=[]
        self.subcategorias=subcategorias
    def incluir(self,categoria):
        subcategorias=[]
        subcategorias.append(categoria)
        self.subcategorias=subcategorias
    pass
      