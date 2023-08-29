class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

ave = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

ave.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(ave.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
print(ave.subcategorias[0].nombre)  # Salida: Passeriformes
