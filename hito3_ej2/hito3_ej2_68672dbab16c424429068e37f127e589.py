class Taxon:

    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=""
    
    def setsubcategorias(self,subcategorias):
        self.subcategorias=subcategorias
        
    def getsubcategorias(self):
        return self.subcategorias
