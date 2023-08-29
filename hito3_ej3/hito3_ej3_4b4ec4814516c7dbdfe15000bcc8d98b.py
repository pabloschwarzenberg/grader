class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
        
    def incluir(self,taxon):
        self.taxon=taxon
        self.subcategorias.append(self.taxon)
 
    def __str__(self):
        return self.categoria+' '+self.nombre