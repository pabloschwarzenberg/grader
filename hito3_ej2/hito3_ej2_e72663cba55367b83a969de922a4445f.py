class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

aves = Taxon("Clase", "Aves")

orden = Taxon("Orden", "Accipitriformes")
familia = Taxon("Familia", "Accipitridae")

aves.subcategorias.append(orden)
aves.subcategorias.append(familia)

print(aves.subcategorias[0].nombre)  # Imprime "Orden"
print(aves.subcategorias[1].nombre)  # Imprime "Familia"