class Taxon:
  def __init__(self,nombre,categoria):
    self.nombre=nombre
    self.categoria=categoria
    self.subcategoria=[]
  def incluir(self,other):
    other.subcategoria.append(self.nombre)
    return other.subcategoria
class Aves:
  def __init__(self,subcategorias):
    self.subcategorias=subcategorias