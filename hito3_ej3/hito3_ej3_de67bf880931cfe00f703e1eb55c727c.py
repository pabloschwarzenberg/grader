class Taxon():
    def __init__(self,categoria,nombre):
        self.categoria="Clase"
        self.nombre="Aves"
        self.subcategorias=[]
        
    def incluir(self,taxon):
        self.subcategorias.append(taxon)
      