class Taxon:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Nivel: {}".format(self.nivel))
        print("Subcategorías: {}".format(self.subcategorias))


if __name__ == "__main__":
    taxon1 = Taxon("Animalia", "Reino")
    taxon2 = Taxon("Chordata", "Filo")
    taxon3 = Taxon("Mammalia", "Clase")
    taxon4 = Taxon("Carnivora", "Orden")

    taxon1.agregar_subcategoria(taxon2)
    taxon2.agregar_subcategoria(taxon3)
    taxon3.agregar_subcategoria(taxon4)

    taxon1.imprimir()
