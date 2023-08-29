class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


# Crear instancias de taxones
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")
reptiles = Taxon("Clase", "Reptiles")

# Agregar subcategorías a Aves
passeriformes = Taxon("Orden", "Passeriformes")
columbiformes = Taxon("Orden", "Columbiformes")

aves.incluir(passeriformes)
aves.incluir(columbiformes)

# Agregar subcategoría a Falconiformes
falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

falconiformes.incluir(halcones)
aves.subcategorias[0].incluir(falconiformes)

# Mostrar información de los taxones y sus subcategorías
print("Taxón:", aves.categoria, "-", aves.nombre)
for subcategoria in aves.subcategorias:
    print("  Subcategoría:", subcategoria.categoria, "-", subcategoria.nombre)
    for subsubcategoria in subcategoria.subcategorias:
        print("    Subsubcategoría:", subsubcategoria.categoria, "-", subsubcategoria.nombre)

print("Taxón:", mamiferos.categoria, "-", mamiferos.nombre)
print("Taxón:", reptiles.categoria, "-", reptiles.nombre)
