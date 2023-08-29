class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Crear instancias de Taxon
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcon = Taxon("Familia", "Halcon")

# Incluir subcategorias
aves.incluir(falconiformes)
falconiformes.incluir(halcon)

# Imprimir subcategorias
print(aves.subcategorias)
print(falconiformes.subcategorias)
