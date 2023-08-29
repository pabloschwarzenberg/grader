class Taxon:
  def __init__(self, categorias):
    self.categorias = []
    
  def incluir(self, taxon):
    self.categorias = self.categorias + taxon
    