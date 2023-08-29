class Taxon:
    def __init__(self,categoria,nombre):
        self.subcategorias=[]
        self.categoria=categoria
        self.nombre=nombre
        
    def __str__(self):
        return self.categoria+" "+nombre+" "+self.subcategorias    
    def incluir(self,other):
        self.subcategorias.append(other)
        
        
    pass
