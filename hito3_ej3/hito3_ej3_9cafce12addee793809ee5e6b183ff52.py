class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
        self.aves=[]
    def incluir(self,ave):
        self.subcategorias.append(ave)
    def imprimir(self):
        print(self.aves)
        