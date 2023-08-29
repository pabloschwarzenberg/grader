class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

if __name__ == "__main__":
    ave = Taxon("Clase", "Aves")
    falconiformes = Taxon("Orden", "Falconiformes")
    ave.incluir(falconiformes)

    print("Categoría:", ave.categoria)
    print("Nombre:", ave.nombre)
    print("Subcategorías:")
    for subcategoria in ave.subcategorias:
        print(" -", subcategoria.categoria, "-", subcategoria.nombre)
