class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre


class RegistroAvistamientos:
    def __init__(self):
        self.avistamientos = []

    def registrar_avistamiento(self, ave):
        self.avistamientos.append(ave)

    def mostrar_avistamientos(self):
        for ave in self.avistamientos:
            print(f"Categoría: {ave.categoria}, Nombre: {ave.nombre}")


# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")

registro = RegistroAvistamientos()

ave1 = Taxon(taxon_aves.categoria, "Ave 1")
ave2 = Taxon(taxon_aves.categoria, "Ave 2")
ave3 = Taxon(taxon_aves.categoria, "Ave 3")

registro.registrar_avistamiento(ave1)
registro.registrar_avistamiento(ave2)
registro.registrar_avistamiento(ave3)

registro.mostrar_avistamientos()

