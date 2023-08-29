class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
       
    def incluir(self,tax):
        self.subcategorias.append(tax)

      
    def __str__(self):
        return "{0},{1},{3}".format(self.categoria,self.nombre,self.subcategorias)


  
      