class Taxon:
  def __init__(self,l1,l2):
    self.categoria = l1
    self.nombre = l2
    self.subcategorias = []
  def incluir(self,taxon2):
    self.subcategorias.append(taxon2)