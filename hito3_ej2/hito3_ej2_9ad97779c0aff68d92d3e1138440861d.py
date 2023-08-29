class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
    self.subcategorias=[]
  
  def __repr__(self):
    return self.categoria,self.nombre,self.subcategorias
      
      
      
      