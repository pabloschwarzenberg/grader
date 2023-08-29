class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.subcategorias=[]
        self.nombre=nombre
    def incluir(self,n):
        self.subcategorias.append(n)
        

      