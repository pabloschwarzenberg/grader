class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")
passeriformes = Taxon("Orden", "Passeriformes")
fringillidae = Taxon("Familia", "Fringillidae")

aves.subcategorias.append(passeriformes)
passeriformes.subcategorias.append(fringillidae)

