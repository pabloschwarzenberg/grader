class Taxon:
  def __init__(self,categoria,nombre):
    self.nombre=nombre
    self.categoria=categoria
    self.subcategorias=[]
  def incluir(self,Taxon):
      self.subcategorias.append(Taxon)
   