class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")

aves.incluir(falconiformes)

print(aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
