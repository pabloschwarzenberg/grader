class Taxon:
  def __init__(self,c,n,subcategorias=[]):
    self.nombre=n
    self.categoria=c
    self.subcategorias=subcategorias

  def incluir(self,orden):
    self.subcategorias.append(orden)
      