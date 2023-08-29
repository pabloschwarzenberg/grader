class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Crear instancias de Taxon para representar las categorías
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

# Construir la jerarquía de clasificación
aves.incluir(falconiformes)
falconiformes.incluir(halcones)

# Ejemplo de impresión de la jerarquía
print(aves.categoria, aves.nombre)
for subcategoria1 in aves.subcategorias:
    print("\t", subcategoria1.categoria, subcategoria1.nombre)
    for subcategoria2 in subcategoria1.subcategorias:
        print("\t\t", subcategoria2.categoria, subcategoria2.nombre)
