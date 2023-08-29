class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
clase_aves = Taxon("Clase", "Aves")
orden_passeriformes = Taxon("Orden", "Passeriformes")
familia_turdidae = Taxon("Familia", "Turdidae")

# Agregar subcategorías
clase_aves.subcategorias.append(orden_passeriformes)
orden_passeriformes.subcategorias.append(familia_turdidae)

# Imprimir las subcategorías
print(clase_aves.subcategorias)                # Salida: [<__main__.Taxon object at 0x00000123456789>]
print(orden_passeriformes.subcategorias)       # Salida: [<__main__.Taxon object at 0x0000012345678A>]

      