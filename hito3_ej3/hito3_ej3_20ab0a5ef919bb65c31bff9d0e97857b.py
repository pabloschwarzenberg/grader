class Taxon:
  def __init__(self,cat,nom,subcategorias=[]):
    self.categoria=cat
    self.nombre=nom
    self.subcategorias=[]
  def incluir(self,taxon):
    self.subcategorias.append(taxon)
      