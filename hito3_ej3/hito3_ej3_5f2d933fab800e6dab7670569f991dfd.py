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

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(aves.subcategorias)  # Imprime una lista con la instancia de falconiformes

print(falconiformes.categoria)  # Imprime "Orden"
print(falconiformes.nombre)  # Imprime "Falconiformes"
print(falconiformes.subcategorias)  # Imprime una lista con la instancia de halcones
