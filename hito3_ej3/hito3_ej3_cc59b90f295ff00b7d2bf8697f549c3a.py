class Taxon:

    def __init__(self, categoria:str , nombre:str):
        subcategorias =[]
        self.categoria = categoria
        self.nombre  = nombre
        self.subcategorias = subcategorias
        
    def incluir(self,Taxon):
        self.subcategorias.append(Taxon)
      
pass    
    