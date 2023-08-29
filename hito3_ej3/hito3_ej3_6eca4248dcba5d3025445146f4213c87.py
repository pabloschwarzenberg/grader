class Taxon:
  def __init__(self,categoria,nombre):
    self.subcategorias=[]
    self.categoria=categoria 
    self.nombre=nombre
  def incluir(self,taxon_aves):
    self.subcategorias.append(taxon_aves)