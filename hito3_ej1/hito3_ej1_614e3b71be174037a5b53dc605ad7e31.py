class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def mostrar(self):
    print("la ave que se ha registrado es: ", self.categoria, self.nombre)
  pass
      