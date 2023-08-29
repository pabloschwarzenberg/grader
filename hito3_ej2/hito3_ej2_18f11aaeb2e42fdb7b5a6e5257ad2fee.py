class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

if __name__ == "__main__":
    ave = Taxon("Clase", "Aves")
    ave.subcategorias.append(Taxon("Orden", "Falconiformes"))
    ave.subcategorias.append(Taxon("Orden", "Psittaciformes"))

    print("Categoría:", ave.categoria)
    print("Nombre:", ave.nombre)
    print("Subcategorías:")
    for subcategoria in ave.subcategorias:
        print(" -", subcategoria.categoria, "-", subcategoria.nombre)
