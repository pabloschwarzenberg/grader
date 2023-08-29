class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))
aves.subcategorias.append(Taxon("Orden", "Psittaciformes"))

print(aves.categoria)                # Salida: Clase
print(aves.nombre)                   # Salida: Aves
print(aves.subcategorias[0].categoria)  # Salida: Orden
print(aves.subcategorias[0].nombre)     # Salida: Falconiformes
print(aves.subcategorias[1].categoria)  # Salida: Orden
print(aves.subcategorias[1].nombre)     # Salida: Psittaciformes
