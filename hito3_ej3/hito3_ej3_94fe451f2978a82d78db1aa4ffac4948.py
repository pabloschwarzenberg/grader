class Taxon:
  def __init__(self, cat, nom):
    self.categoria = cat
    self.nombre = nom
    self.subcategorias = ''
    
  def inlcuir(self, taxon):
    self.subcategorias = taxon
      