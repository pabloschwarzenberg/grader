class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
clase_aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
familia_accipitridae = Taxon("Familia", "Accipitridae")

# Agregar subcategorías utilizando el método incluir
clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(familia_accipitridae)

# Imprimir las subcategorías
print(clase_aves.subcategorias)                # Salida: [<__main__.Taxon object at 0x00000123456789>]
print(orden_falconiformes.subcategorias)       # Salida: [<__main__.Taxon object at 0x0000012345678A>]
