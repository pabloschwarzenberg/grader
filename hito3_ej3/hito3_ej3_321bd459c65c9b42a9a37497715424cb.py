class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
taxon_falconiformes = Taxon("Orden", "Falconiformes")

taxon_aves.incluir(taxon_falconiformes)

print("Categoría:", taxon_aves.categoria)
print("Nombre:", taxon_aves.nombre)
print("Subcategorías:")
for subcategoria in taxon_aves.subcategorias:
    print(" -", subcategoria.categoria, ":", subcategoria.nombre)

      