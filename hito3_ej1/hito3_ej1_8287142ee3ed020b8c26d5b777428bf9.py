class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

ave = Taxon("Clase", "Aves")
mamifero = Taxon("Clase", "Mamíferos")
reptil = Taxon("Clase", "Reptiles")

print(ave.categoria)  # Salida: Clase
print(ave.nombre)  # Salida: Aves
