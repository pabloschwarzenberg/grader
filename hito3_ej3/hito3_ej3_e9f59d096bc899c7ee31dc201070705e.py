class Taxon:
  def __init__(self,categoria, nombre,subcategorias = []):
    self.categoria = categoria
    self.subcategorias = subcategorias
    self.nombre = nombre

  def incluir(self, new_category):
    self.subcategorias.append(new_category)     
      