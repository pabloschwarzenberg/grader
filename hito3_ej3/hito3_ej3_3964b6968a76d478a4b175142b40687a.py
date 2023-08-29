class Taxon:
    def __init__(self, nuevacategoria, nuevonombre):
        self.categoria = nuevacategoria
        self.nombre = nuevonombre
        self.subcategorias = []
    #def setsubcategorias(self, nuevasubcategorias):
        
    def incluir(self, nuevasubcategorias):
        self.subcategorias.append(nuevasubcategorias)