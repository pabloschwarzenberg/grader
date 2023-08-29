class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        subcategorias=[]
        self.subcategorias=subcategorias
        self.Taxon=Taxon
    def incluir(self,Taxon):
        self.subcategorias.append(Taxon)    
    def mostrar(self):
        print(self.categoria,self.nombre,self.subcategorias,self.Taxon)

      