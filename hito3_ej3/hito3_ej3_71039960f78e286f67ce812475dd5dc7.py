class Taxon:
  
  def __init__(self,categoria,nombre,subcategorias=[]):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategorias = []

  def incluir(self,tax):
      self.subcategorias.append(tax)