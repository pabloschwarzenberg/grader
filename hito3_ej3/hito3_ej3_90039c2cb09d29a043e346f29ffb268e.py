class Taxon:
  def __init__(self,categoria,nombre):
    self.nombre=nombre
    self.categoria=categoria
    subcategorias=[]
    self.subcategorias=subcategorias
     
  def incluir(self,categoria):
    subcategorias=[]
    subcategorias.append(categoria)
    self.subcategorias=subcategorias