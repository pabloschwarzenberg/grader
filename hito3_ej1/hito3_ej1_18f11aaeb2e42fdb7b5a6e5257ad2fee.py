class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

if __name__ == "__main__":
    ave = Taxon("Clase", "Aves")
    print("Categoría:", ave.categoria)
    print("Nombre:", ave.nombre)
