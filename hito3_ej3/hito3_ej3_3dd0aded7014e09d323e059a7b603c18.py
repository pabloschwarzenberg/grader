class Taxon:
  def __init__(self,categoria,nombre,subcategoria=[]):
    self.nombre = nombre
    self.categoria=categoria
    self.subcategorias=subcategoria

  def incluir(self,subcategoria):
    self.subcategorias.append(subcategoria)
    