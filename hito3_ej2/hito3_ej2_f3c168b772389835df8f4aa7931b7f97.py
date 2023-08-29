class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")

passeriformes = Taxon("Orden", "Passeriformes")
falconiformes = Taxon("Orden", "Falconiformes")

aves.subcategorias.append(passeriformes)
aves.subcategorias.append(falconiformes)
      