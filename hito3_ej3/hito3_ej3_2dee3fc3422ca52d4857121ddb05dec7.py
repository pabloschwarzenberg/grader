class Taxon:
    subcategorias=[]
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
    def incluir(self,elemento):
        self.subcategorias.append(elemento)