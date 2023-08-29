class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
taxon_aves.subcategorias.append(Taxon("Orden", "Passeriformes"))
taxon_aves.subcategorias.append(Taxon("Orden", "Falconiformes"))

print("Categoría:", taxon_aves.categoria)
print("Nombre:", taxon_aves.nombre)
print("Subcategorías:")
for subcategoria in taxon_aves.subcategorias:
    print(" -", subcategoria.categoria, ":", subcategoria.nombre)
