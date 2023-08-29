class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria= categoria
        self.nombre = nombre
        self.subcategorias = []
    def incluir(self,taxon):
        self.taxon= taxon
        self.subcategorias= self.subcategorias+[taxon]
        return self.subcategorias