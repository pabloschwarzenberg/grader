class Taxon:
    def _init_(self,nombre,categoria):
        self.nombre='Aves'
        self.categoria='Clase'
        self.subcategorias=[]
        
    def setNombre(self,n):
        self.nombre = n
    def setCategoria(self,c):
        self.categoria = c
    def setSubcategorias(self,s):
        self.subcategorias = s

    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria
    def getSubcategorias(self):
        return self.subcategorias
        
    def _str_(self):
        return nombre,categoria