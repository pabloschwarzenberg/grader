class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
  def incluir (self,otro_taxon):
    self.subcategorias.append(otro_taxon)
 