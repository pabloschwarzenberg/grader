class Taxon:
  def __init__(self,categoria, nombre,subcategorias = []):
    self.categoria = categoria
    self.subcategorias = subcategorias
    self.nombre = nombre
  def incluir(self, incluir):
    self.subcategorias.append(incluir)
      