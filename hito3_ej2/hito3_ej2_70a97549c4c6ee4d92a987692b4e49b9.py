class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
aves = Taxon("Clase", "Aves")

orden1 = Taxon("Orden", "Falconiformes")
orden2 = Taxon("Orden", "Psittaciformes")

aves.subcategorias.append(orden1)
aves.subcategorias.append(orden2)
    