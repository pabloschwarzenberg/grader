class Taxon:
  def __init__(self, categoria, nombre):
    self.nombre = nombre
    self.categoria = categoria
aves = Taxon("Clase", "Aves")
print(aves.categoria)
print(aves.nombre)