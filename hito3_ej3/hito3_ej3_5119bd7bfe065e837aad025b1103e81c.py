class Taxon:
    def __init__(self,a,b):
        self.categoria=a
        self.nombre=b
        self.subcategorias=[]
    
    def incluir(self,taxon):
        self.subcategorias.append(taxon)