class Taxon:
    def __init__(self,nombre,categoria):
        self.nombre='Aves'
        self.categoria='Clase'
        self.subcategorias=[]
        
    def setNombre(self,n):
        self.nombre = n
    def setCategoria(self,c):
        self.categoria = c
    def setsubcategorias(self,s):
        self.subcategorias = s

    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria
    def getSubcategorias(self):
        return self.subcategorias
        
    def __str__(self):
        return nombre,categoria
        subcategorias=[]
class Taxon:
  def __init__(self,c,n,):
    self.categoria=c
    self.nombre=n
    self.subcategorias=subcategorias
  def incluir(self,orden):
    self.subcategorias.append(orden)


      
