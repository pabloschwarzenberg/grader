class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

    def mostrar_informacion(self):
        print("Categoría: {}".format(self.categoria))
        print("Nombre: {}".format(self.nombre))


taxon1 = Taxon("Mamífero", "León")
taxon2 = Taxon("Ave", "Águila")

taxon1.mostrar_informacion()
taxon2.mostrar_informacion()
