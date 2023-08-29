class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcon = Taxon("Familia", "Halcon")
halcon.incluir(Taxon("Género", "Falco"))
falconiformes.incluir(halcon)
aves.incluir(falconiformes)

print(aves.subcategorias)                   
print(aves.subcategorias[0].subcategorias)
print(aves.subcategorias[0].subcategorias[0].subcategorias)