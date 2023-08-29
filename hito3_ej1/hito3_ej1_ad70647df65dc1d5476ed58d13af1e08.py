class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
      
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")
reptiles = Taxon("Clase", "Reptiles")


print(aves.categoria)  # Imprime "Clase"
print(mamiferos.nombre)  # Imprime "Mamíferos"
print(reptiles.categoria)  # Imprime "Clase"
