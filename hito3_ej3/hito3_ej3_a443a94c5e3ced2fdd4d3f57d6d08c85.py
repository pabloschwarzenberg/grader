class Taxon():
  def __init__(self, categoria, nombre):
    self.categoria= categoria #clase
    self.nombre= nombre #aves
    self.subcategorias= []

  def incluir(self, x):
    self.subcategorias.append(x)
      