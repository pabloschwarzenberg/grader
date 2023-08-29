class Taxon:
    def __init__(self, nombre_cientifico, nombre_comun, familia, orden, clase):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.familia = familia
        self.orden = orden
        self.clase = clase

    def mostrar_informacion(self):
        print("Nombre científico:", self.nombre_cientifico)
        print("Nombre común:", self.nombre_comun)
        print("Familia:", self.familia)
        print("Orden:", self.orden)
        print("Clase:", self.clase)


# Ejemplo de uso
ave = Taxon("Parus major", "Carbonero Común", "Paridae", "Passeriformes", "Aves")
ave.mostrar_informacion()

      