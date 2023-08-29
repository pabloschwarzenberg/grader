class Taxon:
  def __init__(self,categoria,nombre):
    global subcategorias
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]      