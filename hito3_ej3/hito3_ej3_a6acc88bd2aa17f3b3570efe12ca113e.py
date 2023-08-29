class Taxon:
    def __init__(self,ctg,name):
        self.categoria=ctg
        self.nombre=name
        self.subcategorias=[]
    def incluir(self,grupo):
        self.subcategorias.append(grupo)