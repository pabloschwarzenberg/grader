class Taxon:
    def __init__(self,categoria,nombre):
        subcategorias=[]
        self.subcategorias=subcategorias
        self.categoria=categoria
        self.nombre=nombre
    def incluir(self,incluir):
        self.subcategorias.append(incluir)
        return subcategorias