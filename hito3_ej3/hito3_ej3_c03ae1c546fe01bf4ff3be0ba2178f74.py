class Taxon:
  def __init__(self,categoria,nombre):
    if isinstance(categoria,str) == True and isinstance(nombre,str) == True:
      self.categoria=categoria
      self.nombre=nombre
      self.subcategorias=[]
  def incluir(self,grupo):
    if isinstance(grupo,Taxon) == True:
      self.subcategorias.append(grupo)