class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(len(aves.subcategorias))  # Imprime 2
print(aves.subcategorias[0].nombre)  # Imprime "Falconiformes"
print(aves.subcategorias[1].nombre)  # Imprime "Passeriformes"