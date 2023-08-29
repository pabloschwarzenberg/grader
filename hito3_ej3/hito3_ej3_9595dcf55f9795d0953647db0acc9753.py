class Taxon:
  def __init__(self,categoria,nombre,subcategorias=[]):
    self.nombre=nombre
    self.categoria=categoria
    self.subcategorias=subcategorias
    
class Aves(Taxon, "Falconiformes","","Halcones"):
    pass