class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Crear los taxones
aves = Taxon("Clase Aves")
falconiformes = Taxon("Orden Falconiformes")
halcones = Taxon("Halcones")

# Agregar falconiformes como subcategoría de aves
aves.incluir(falconiformes)

# Agregar halcones como subcategoría de falconiformes
falconiformes.incluir(halcones)

# Verificar la estructura de taxones
print(aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(falconiformes.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]

