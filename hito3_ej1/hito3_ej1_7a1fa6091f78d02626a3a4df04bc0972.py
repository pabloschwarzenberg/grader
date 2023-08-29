class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre


# Crear instancias de taxones
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")
reptiles = Taxon("Clase", "Reptiles")

# Mostrar información de los taxones
print("Taxón:", aves.categoria, "-", aves.nombre)
print("Taxón:", mamiferos.categoria, "-", mamiferos.nombre)
print("Taxón:", reptiles.categoria, "-", reptiles.nombre)

      