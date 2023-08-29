class Taxon:

    categoria = ""
    nombre = ""

    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

    def obtener_subcategorias(self):
        return self.subcategorias


aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")

aves.incluir(falconiformes)

if __name__ == "__main__":
    print(aves.obtener_subcategorias())