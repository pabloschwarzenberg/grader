class Taxon:
  def __init__(self, categoria, nombre):
    "Constructor de un taxon"
    self.categoria = categoria
    self.nombre = nombre
    self.subcategorias = [] 
      