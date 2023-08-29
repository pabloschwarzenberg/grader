class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def setCat(self,categoria):
    self.categoria=categoria
  def setNom(self,nombre):
    self.nombre=nombre
  def getCat(self,categoria):
    return self.categoria
  def getNom(self,nombre):
    return self.nombre
      