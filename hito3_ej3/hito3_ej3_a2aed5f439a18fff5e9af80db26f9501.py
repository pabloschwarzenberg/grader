class Taxon:
  def __init__(self, categoria, nombre,subcategorias=[]):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategorias=subcategorias
  def incluir(self,subcategorias):
      self.subcategorias.append(subcategorias)