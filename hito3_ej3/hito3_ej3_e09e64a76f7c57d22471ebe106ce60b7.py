class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Ejemplo de uso
clase_aves = Taxon("Clase Aves")
orden_falconiformes = Taxon("Orden Falconiformes")
halcones = Taxon("Halcones")

# Añadir el taxón Orden Falconiformes como subcategoría de Clase Aves
clase_aves.incluir(orden_falconiformes)

# Añadir el taxón Halcones como subcategoría de Orden Falconiformes
orden_falconiformes.incluir(halcones)

# Verificar la estructura
print(clase_aves.nombre)
# Salida: Clase Aves
print(clase_aves.subcategorias[0].nombre)
# Salida: Orden Falconiformes
print(clase_aves.subcategorias[0].subcategorias[0].nombre)
# Salida: Halcones
