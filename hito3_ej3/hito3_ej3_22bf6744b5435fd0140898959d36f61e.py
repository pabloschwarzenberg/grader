class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]  
        
    def incluir(self,categoria):
        self.subcategorias.append(categoria)

    def __str__(self):
        return(self.categoria+" "+self.subcategorias+" "+self.nombre)
      