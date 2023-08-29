class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias = []
    def __str__(self):
        "{0},{1},{2}".format(self.categoria,self.nombre)
        
    
        
      
    
      