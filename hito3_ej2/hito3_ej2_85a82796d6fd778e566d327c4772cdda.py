class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
aves = Taxon("Clase", "Aves")

# Crear subcategorías
passeriformes = Taxon("Orden", "Passeriformes")
falconiformes = Taxon("Orden", "Falconiformes")

# Agregar subcategorías al taxón "Aves"
aves.subcategorias.append(passeriformes)
aves.subcategorias.append(falconiformes)
