class Taxon:
    def __init__ (self,nuevaCategoria,nuevoNombre):
        self.categoria=nuevaCategoria
        self.nombre=nuevoNombre
        self.subcategorias=[]
    
    def getCategoria(self):
        return self.categoria
    
    def getNombre(self):
        return self.nombre
    
    def setCategoria(self,nuevaCategoria):
        self.categoria=nuevaCategoria
    
    def setNombre(self,nuevoNombre):
        self.nombre=nuevoNombre
      
    def getSubcategorias(self):
        return self.subcategorias
        
    def setSubcategorias(self,nuevaSubcategorias):
        self.subcategorias=nuevaSubcategorias

    def incluir(self,taxon):
        self.subcategorias.append(taxon)

      