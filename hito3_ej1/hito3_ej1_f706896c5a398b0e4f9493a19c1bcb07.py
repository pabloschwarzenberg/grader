class Taxon:

  def __init__(self,nombre,categoria):
    self.nombre=nombre
    self.categoria=categoria

class Aves(Taxon):

  def __init__(self):
    self.nombre="Aves"
    self.categoria="Clase"
