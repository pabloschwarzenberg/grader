class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
        
    def getCategoria(self):
        return self.categoria
    
    def getNombre(self):
        return self.nombre
        
    def subcategorias(self):
        return self.subcategorias
    
    def __str__(self):
        return self.categoria+","+self.nombre+","+self.subcategorias
        

      