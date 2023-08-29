class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")

aves.subcategorias.append(falconiformes)
