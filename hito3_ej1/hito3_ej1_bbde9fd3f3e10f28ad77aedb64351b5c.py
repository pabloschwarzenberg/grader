class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria = categoria
    self.nombre = nombre
  def getCategoria(self):
    return self.categoria

  def getNombre(self):
    return self.nombre

  def __str__(self):
    return self.categoria+" "+self.nombre