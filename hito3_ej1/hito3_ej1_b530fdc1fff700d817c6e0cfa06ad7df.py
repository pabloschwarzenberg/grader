#Ornitología 1, 2 y 3 - 3/3 point (TOTAL)
class Taxon():
  def _init_(self, categoria, nombre):
    self.categoria = categoria  # clase
    self.nombre = nombre  # aves
    self.subcategorias = []

  def incluir(self, x):
    self.subcategorias.append(x)
    

    