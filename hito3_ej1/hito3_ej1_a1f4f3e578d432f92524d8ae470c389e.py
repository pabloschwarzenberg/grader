class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def mostrar(self):
    print("La ave registrada es", self.categoria,self.nombre)
  pass
