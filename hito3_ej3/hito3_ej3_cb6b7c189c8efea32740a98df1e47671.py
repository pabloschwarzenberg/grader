class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
  
  def incluir(self,taxon):
    self.subcategorias.append(taxon)
      