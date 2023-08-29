class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
  def subcategorias(self,subcategoria):
    self.subcategoria=subcategoria
  def incluir(self,parametro):
    self.subcategorias.append(parametro)