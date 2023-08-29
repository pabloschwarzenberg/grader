class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

taxon_aves = Taxon("Clase", "Aves")
taxon_falconiformes = Taxon("Orden", "Falconiformes")

taxon_aves.incluir(taxon_falconiformes)
print(taxon_aves.subcategorias) 