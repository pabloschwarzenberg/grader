class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
aves.incluir(falconiformes)

print(aves.categoria)  # Salida: Clase
print(aves.nombre)  # Salida: Aves
print(len(aves.subcategorias))  # Salida: 1
print(aves.subcategorias[0].categoria)  # Salida: Orden
print(aves.subcategorias[0].nombre)  # Salida: Falconiformes      