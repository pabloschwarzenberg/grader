class Taxon:
  def __init__(self,categoria,nombre):
    self.subcategorias = []
    self.categoria = str(categoria)
    self.nombre = str(nombre)
    
  def incluir(self,Taxon):
    self.subcategorias.append(Taxon)