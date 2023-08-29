class Taxon():
  def __init__(self,categoria,nombre,subcategoria):
    self.nombre=nombre
    self.categoria=categoria
    self.subcategoria=subcategoria

  def mostrar(self):
    print(self.nombre,self.categoria,self.subcategoria)