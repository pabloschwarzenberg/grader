class Taxon:
  def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre =  nombre
    lista=[]
    self.subcategorias = lista    
  def incluir(self, subcategorias):
    self.subcategorias.append(subcategorias)
    pass
     