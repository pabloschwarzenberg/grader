class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

ave = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
halcon = Taxon("Familia", "Halconidae")

ave.incluir(orden)
orden.incluir(halcon)

print(ave.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
print(ave.subcategorias[0].nombre)  # Salida: Falconiformes
