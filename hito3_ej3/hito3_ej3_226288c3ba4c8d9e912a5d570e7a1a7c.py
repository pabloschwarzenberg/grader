class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


# Ejemplo de uso
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

aves.incluir(falconiformes)
falconiformes.incluir(halcones)

# Imprimir información
print(aves.categoria)  # Imprime: Clase
print(aves.nombre)  # Imprime: Aves
print(aves.subcategorias[0].categoria)  # Imprime: Orden
print(aves.subcategorias[0].nombre)  # Imprime: Falconiformes
print(aves.subcategorias[0].subcategorias[0].categoria)  # Imprime: Familia
print(aves.subcategorias[0].subcategorias[0].nombre)  # Imprime: Halcones