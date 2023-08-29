class Taxon:
  def __init__(self,nombre,categoria):
    self.nombre = 'Aves'
    self.categoria = 'Clase'
    self.subcategorias = []
  def incluir(self,subcat):
    self.subcategorias.append(subcat)