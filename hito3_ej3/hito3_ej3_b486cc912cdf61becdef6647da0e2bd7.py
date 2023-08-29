class Taxon():
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
  def print(self):
    print(self.categoria,",",self.nombre,",",self.subcategorias)
  def incluir(self,taxon):
    self.taxon=taxon
    self.subcategorias.append(taxon)
