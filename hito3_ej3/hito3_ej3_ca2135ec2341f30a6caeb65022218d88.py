class Taxon:
    def __init__(self, c, n):
        self.categoria = c
        self.nombre = n
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

if __name__ == "__main__":
    ave = Taxon("Clase", "Aves")
    orden = Taxon("Orden", "Falconiformes")
    halcon = Taxon("Familia", "Halcones")

    ave.incluir(orden)
    orden.incluir(halcon)

    print("Ave:", ave.nombre)
    print("Subcategorías de Aves:", [sub.nombre for sub in ave.subcategorias])
    print("Orden:", orden.nombre)
    print("Subcategorías de Falconiformes:", [sub.nombre for sub in orden.subcategorias])