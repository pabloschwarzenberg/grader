class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []


# Crear instancias de taxones
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")
reptiles = Taxon("Clase", "Reptiles")

# Agregar subcategorías a Aves
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))
aves.subcategorias.append(Taxon("Orden", "Columbiformes"))

# Mostrar información de los taxones y sus subcategorías
print("Taxón:", aves.categoria, "-", aves.nombre)
for subcategoria in aves.subcategorias:
    print("  Subcategoría:", subcategoria.categoria, "-", subcategoria.nombre)

print("Taxón:", mamiferos.categoria, "-", mamiferos.nombre)
print("Taxón:", reptiles.categoria, "-", reptiles.nombre)

      