subcategorias=[]
class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=subcategorias
    
  def incluir(self,categoria):
    subcategorias.append(self)