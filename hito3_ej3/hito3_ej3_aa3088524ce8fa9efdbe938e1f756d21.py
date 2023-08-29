class Taxon:
  def __init__(self, categoria, nombre):
     self.categoria = categoria
     self.nombre = nombre
     self.subcategorias = []
  def incluir(self, taxon):
     self.subcategorias.append(taxon)

#principal
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")

aves.incluir(falconiformes)

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(len(aves.subcategorias))  # Imprime 1
print(aves.subcategorias[0].nombre)  # Imprime "Falconiformes"