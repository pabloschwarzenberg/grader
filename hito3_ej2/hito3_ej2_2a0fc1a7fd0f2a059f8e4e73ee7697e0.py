class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
        
aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))