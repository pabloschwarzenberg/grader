class Taxon:
  def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre = nombre
    self.subcategorias = []

taxon = Taxon("Clase", "Aves")
print(taxon.categoria)
print(taxon.nombre)
print(taxon.subcategorias)