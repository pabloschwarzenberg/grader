nombre=""
categoria=""
class Taxon:
  def __init__(self,nombre,categoria):
    self.nombre = "Aves"
    self.categoria = "Clase"
    pass
    
class Aves(Taxon):
   def __init__(nombre,categoria):
      super().__init__(nombre,categoria)