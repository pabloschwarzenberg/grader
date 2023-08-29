class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(aves.subcategorias)  # Imprime []

reptiles = Taxon("Clase", "Reptiles")
aves.subcategorias.append(reptiles)
print(aves.subcategorias)  # Imprime [reptiles]

