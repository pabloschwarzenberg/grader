class Taxon():
  categoria = ""
  nombre = ""
  subcategorias = []
  
  def __init__(self,categoria,nombre,subcategorias):
    self.categoria = categoria
    self.nombre = nombre
    self.subcategorias = subcategorias