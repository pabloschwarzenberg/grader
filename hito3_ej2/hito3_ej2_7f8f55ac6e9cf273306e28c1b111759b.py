class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
    self.aves=[]
  def obtener_aves(self,ave):
    self.aves.append(ave)
  def imprimirlo(self):
    print(self.aves)

      