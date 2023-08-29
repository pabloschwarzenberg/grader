class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Crear un objeto Taxon para la Clase Aves
aves = Taxon("Clase", "Aves")

# Crear un objeto Taxon para el Orden Falconiformes
falconiformes = Taxon("Orden", "Falconiformes")

# Agregar el taxón de Falconiformes como subcategoría de Aves
aves.incluir(falconiformes)

# Acceder a los atributos
print(aves.categoria)           # Salida: Clase
print(aves.nombre)              # Salida: Aves
print(aves.subcategorias)       # Salida: [<__main__.Taxon object at 0x7f7b9d3f6d30>]
print(aves.subcategorias[0])    # Salida: <__main__.Taxon object at 0x7f7b9d3f6d30>
print(falconiformes.categoria)   # Salida: Orden
print(falconiformes.nombre)      # Salida: Falconiformes
