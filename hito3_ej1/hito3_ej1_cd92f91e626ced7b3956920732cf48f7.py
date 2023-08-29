class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre


if __name__ == "__main__":
    taxon = Taxon("Clase", "Aves")
    print("Categoría:", taxon.categoria)
    print("Nombre:", taxon.nombre)
