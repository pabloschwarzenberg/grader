class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


if __name__ == "__main__":
    clase_aves = Taxon("Clase", "Aves")
    orden_falconiformes = Taxon("Orden", "Falconiformes")
    familia_accipitridae = Taxon("Familia", "Accipitridae")

    clase_aves.incluir(orden_falconiformes)
    orden_falconiformes.incluir(familia_accipitridae)

    print("Categoría:", clase_aves.categoria)
    print("Nombre:", clase_aves.nombre)
    print("Subcategorías:", len(clase_aves.subcategorias))
    print("Subcategoría 1:", clase_aves.subcategorias[0].nombre)
    print("Subcategorías de la subcategoría 1:", len(orden_falconiformes.subcategorias))
