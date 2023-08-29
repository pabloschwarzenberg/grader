class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso de la clase Taxon
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcon = Taxon("Familia", "Halcones")

aves.incluir(falconiformes)  # Agrega el taxon Falconiformes a la lista de subcategorias de Aves
falconiformes.incluir(halcon)  # Agrega el taxon Halcones a la lista de subcategorias de Falconiformes

print(aves.subcategorias)  # Imprime [falconiformes]
print(falconiformes.subcategorias)  # Imprime [halcon]
print(halcon.subcategorias)  # Imprime []
