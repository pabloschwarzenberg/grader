class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        subcategorias=[]
        self.subcategorias=subcategorias
    def mostrar(self):
        print(self.categoria,self.nombre,self.subcategorias)
      