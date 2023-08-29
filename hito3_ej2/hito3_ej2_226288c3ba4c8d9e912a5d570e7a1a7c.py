class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

# Imprimir información
print(aves.categoria)  # Imprime: Clase
print(aves.nombre)  # Imprime: Aves
print(aves.subcategorias[0].categoria)  # Imprime: Orden
print(aves.subcategorias[0].nombre)  # Imprime: Passeriformes
print(aves.subcategorias[0].subcategorias[0].categoria)  # Imprime: Familia
print(aves.subcategorias[0].subcategorias[0].nombre)  # Imprime: Turdidae