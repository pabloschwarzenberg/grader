class Taxon:
   def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre = nombre
    self.subcategorias=[]    

   def incluir(self, x):
    self.subcategorias=[] 
    self.subcategorias.append(x)
      
      