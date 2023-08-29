class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Creación de instancias de Taxon
aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
familia_halcones = Taxon("Familia", "Halcones")

# Establecimiento de relaciones jerárquicas
aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(familia_halcones)

# Impresión de los valores de los atributos
print(aves.categoria)  # Salida: Clase
print(aves.nombre)  # Salida: Aves
print(aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]

print(orden_falconiformes.categoria)  # Salida: Orden
print(orden_falconiformes.nombre)  # Salida: Falconiformes
print(orden_falconiformes.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]

print(familia_halcones.categoria)  # Salida: Familia
print(familia_halcones.nombre)  # Salida: Halcones
print(familia_halcones.subcategorias)  # Salida: []