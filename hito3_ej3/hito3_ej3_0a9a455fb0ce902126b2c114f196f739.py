class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria = categoria 
    self.nombre = nombre
    self.subcategorias = list()
  def __str__(self):
    return "la",self.nombre, "es de la categoria", self.categoria
  def incluir(self,taxon):
    self.subcategorias.append(taxon)