class Taxon:
  def __init__(self,categoria,nombre):
      self.categoria=categoria
      self.nombre=nombre
      self.subcategorias=[]
  def incluir(self,taxon):
      self.subcategorias.append(taxon)
      return subcategorias
  def __str__(self):
      return "{0},{1}".format(self.categoria,self.nombre)
      