class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))

print(aves.categoria)            # "Clase"
print(aves.nombre)               # "Aves"
print(len(aves.subcategorias))   # 2
print(aves.subcategorias[0].nombre)   # "Falconiformes"
print(aves.subcategorias[1].nombre)   # "Passeriformes"

      