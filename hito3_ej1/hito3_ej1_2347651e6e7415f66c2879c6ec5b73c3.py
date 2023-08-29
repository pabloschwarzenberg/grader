class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")
genero = Taxon("Genero", "Turdus")

      