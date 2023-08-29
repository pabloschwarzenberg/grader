class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))

print(aves.categoria)  # Salida: Clase
print(aves.nombre)  # Salida: Aves
print(len(aves.subcategorias))  # Salida: 2
print(aves.subcategorias[0].categoria)  # Salida: Orden
print(aves.subcategorias[0].nombre)  # Salida: Passeriformes
print(aves.subcategorias[1].categoria)  # Salida: Orden
print(aves.subcategorias[1].nombre)  # Salida: Falconiformes      