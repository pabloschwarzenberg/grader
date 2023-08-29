class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategoria = []
    
    def setCategoria(self, categoria):
        self.categoria = categoria
    def setNombre(self, nombre):
        self.nombre = nombre
    def setSubcategoria(self, subcategoria):
        self.subcategoria = subcategoria

    def getCategoria(self):
        return self.categoria
    def getNombre(self):
        return self.nombre
    def getSubcategoria(self):
        return self.subcategoria

    def __str__(self):
        retorno = self.categoria + self.nombre + self.subcategoria
        return retorno
pass
      