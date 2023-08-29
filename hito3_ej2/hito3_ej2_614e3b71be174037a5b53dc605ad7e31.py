class Taxon:
  subcategorias=[]
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def agregar_subcategorias(self,subcategorias):
      self.categorias.append(subcategorias)
  def mostrar(self):
    print("la ave que se ha registradao es: ", self.categoria,self.subcategorias, self.nombre)
  pass
      