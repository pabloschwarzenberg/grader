class Taxon:
    def __init__(self, categoria, nombre): 
        self.c = categoria
        self.n = nombre
    

    def incluir(self, taxon):
        self.t = taxon
        self.subcategoria = []
        self.subcategoria.append(taxon)
        return self.subcategoria