class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []  #lista vacía
    
    def incluir(self, taxon):
        self.subcategorias.append(taxon)
    
aves = Taxon("Clase", "Aves")
aves.incluir(Taxon("Orden", "Falconiformes"))