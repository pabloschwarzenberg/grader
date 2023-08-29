class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
        
    def incluir(self,Taxon):
        self.subcategorias=[]
        self.subcategorias.append(Taxon)
    
    def __str__(self):
        return "{0},{1},{2}".format(self.categoria,self.nombre,self.subcategorias)

   
ave1=Taxon("","")
print(ave1)
      
      