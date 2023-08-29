class Taxon:
  def __init__(self,categoria,nombre):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategoria = []

  def incluir(self,unTaxon):
      self.subcategoria.append(unTaxon)