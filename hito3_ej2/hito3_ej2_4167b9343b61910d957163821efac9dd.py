class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")

print(aves.categoria)  # Output: Clase
print(aves.nombre)  # Output: Aves
print(aves.subcategorias)  # Output: []
