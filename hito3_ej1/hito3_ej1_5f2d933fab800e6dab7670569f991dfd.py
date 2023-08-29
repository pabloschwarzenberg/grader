class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"

print(mamiferos.categoria)  # Imprime "Clase"
print(mamiferos.nombre)  # Imprime "Mamíferos"
