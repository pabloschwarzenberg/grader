class Taxon:
  def __init__(self,cat,nombre):
    self.categoria = cat
    self.nombre =  nombre
    self.subcategorias=[]
  def incluir(self,taxon):
    self.subcategorias.append(taxon)