class Taxon:
  def __init__(self,subcategorias,categoria):
    self.nombre = "Aves"
    self.categoria = "Clase"
    self.subcategorias = []
    
  def incluir(self,ave):
    self.subcategorias.append(ave)