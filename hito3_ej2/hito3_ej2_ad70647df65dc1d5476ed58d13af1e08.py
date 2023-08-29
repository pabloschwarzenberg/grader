class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))
aves.subcategorias.append(Taxon("Orden", "Columbiformes"))

print(aves.subcategorias[0].nombre)  # Imprime "Passeriformes"
print(aves.subcategorias[1].nombre)  # Imprime "Columbiformes"
