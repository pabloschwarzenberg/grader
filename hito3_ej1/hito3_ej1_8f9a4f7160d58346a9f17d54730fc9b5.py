class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

if __name__ == "__main__":
    aves = Taxon("Clase", "Aves")
    print("Categoría:", aves.categoria)
    print("Nombre:", aves.nombre)