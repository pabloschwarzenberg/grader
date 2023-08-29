class Taxon():
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def print(self):
    print(self.categoria,",",self.nombre)
