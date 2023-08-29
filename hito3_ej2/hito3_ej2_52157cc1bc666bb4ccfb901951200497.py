class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def mostrar_informacion(self):
        print("Categoría: {}".format(self.categoria))
        print("Nombre: {}".format(self.nombre))
        print("Subcategorías:")
        for subcategoria in self.subcategorias:
            print("- {}".format(subcategoria.nombre))


ave = Taxon("Clase Aves", "Águila Real")
ave.agregar_subcategoria(Taxon("Orden Falconiformes", "Falconidae"))
ave.agregar_subcategoria(Taxon("Orden Falconiformes", "Accipitridae"))

ave.mostrar_informacion()
