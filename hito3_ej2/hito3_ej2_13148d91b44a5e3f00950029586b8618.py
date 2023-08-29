class Taxon:
    def __init__(self, nombre_cientifico, nombre_comun, familia, orden, clase):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.familia = familia
        self.orden = orden
        self.clase = clase
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def mostrar_informacion(self):
        print("Nombre científico:", self.nombre_cientifico)
        print("Nombre común:", self.nombre_comun)
        print("Familia:", self.familia)
        print("Orden:", self.orden)
        print("Clase:", self.clase)

        if self.subcategorias:
            print("Subcategorías:")
            for subcategoria in self.subcategorias:
                subcategoria.mostrar_informacion()


# Ejemplo de uso
ave = Taxon("Parus major", "Carbonero Común", "Paridae", "Passeriformes", "Aves")

subcategoria1 = Taxon("Parus major sub1", "Carbonero sub1", "Paridae sub1", "Passeriformes sub1", "Aves sub1")
subcategoria2 = Taxon("Parus major sub2", "Carbonero sub2", "Paridae sub2", "Passeriformes sub2", "Aves sub2")

ave.agregar_subcategoria(subcategoria1)
ave.agregar_subcategoria(subcategoria2)

ave.mostrar_informacion()
