class Taxon:
  subcategorias=[]
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def add_subcategorias(self,subcategorias):
      self.categorias.append(subcategorias)
  def mostrar(self):
    print("el animal registrado es", self.categoria,self.subcategorias, self.nombre)
pass