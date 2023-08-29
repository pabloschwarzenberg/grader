class Taxon:
  taxon=[]
  def __init__(self,categoria,nombre):
        self.categoria= categoria
        self.nombre= nombre
        self.subcategorias = []
  def incluir(self,Taxon):
        self.subcategorias.append(Taxon)
        
        
 
        
  
      